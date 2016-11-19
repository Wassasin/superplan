from __future__ import print_function
from flask import Flask, jsonify, request
import sys
import datetime
from server import config, plan
from server.apis import geo
from data import Prompt

# Mocking for demo
from server import (
    mock, mock_scenario2
)

global timeline
timeline = None

global prompt_generator
prompt_generator = None

global commutePlanner
commutePlanner = None

def debug(obj):
    print(obj, file=sys.stderr)


app = Flask("superplan")

def object_to_dict(obj):
    """Utility function for converting class objects to dictionaries."""
    if isinstance(obj, datetime.timedelta):
        return obj.seconds

    if not hasattr(obj, "__dict__"):
        return obj

    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(object_to_dict(item))
        else:
            element = object_to_dict(val)
        result[key] = element
    return dict(result)


@app.route("/")
def root():
    return jsonify(
        msg="Welcome! "
            "See https://github.com/Wassasin/superplan for my interface.")


@app.route("/schedule", methods=["GET"])
def getSchedule():
    time = request.args.get('time', None)
    if time is not None:
        hours = time[:2]
        minutes = time[3:5]
        time = datetime.time(hour=int(hours), minute=int(minutes))

    conf = config.Config()
    g = geo.Geo(conf.get('google-key'))

    concrete_timeline = plan.plan(timeline, g, commutePlanner).events
    my_prompts = []
    for e in concrete_timeline:
        if e.description == "sleep":
            e.duration -= datetime.timedelta(minutes=30)
            p = Prompt(e.startTime + e.duration, "Wake up", ["I have awoken"])

            if time is not None:
                # Do mocking.
                mockp = prompt_generator(time)
                if mockp is not None:
                    p.description = mockp.description
                    p.answers = mockp.answers

            my_prompts.append(p)

    prompts = map(object_to_dict, my_prompts)
    events = map(object_to_dict, concrete_timeline)

    return jsonify(events=events, prompts=prompts)


@app.route("/resolve/<int:eventId>/cancel", methods=["POST"])
def resolveCancel(eventId):
    return jsonify(action="resolveCancel", eventId=eventId)


@app.route("/resolve/<int:eventId>/move", methods=["POST"])
def resolveMove(eventId):
    newTime = request.json["newTime"]
    return jsonify(action="resolveMove", eventId=eventId, newTime=newTime)


def select_scenario(scenario_nr=0):
    if scenario_nr == 0:
        return mock.timeline, mock.prompt_generator
    if scenario_nr == 1:
        raise NotImplementedError
    if scenario_nr == 2:
        return mock_scenario2.timeline, mock_scenario2.prompt_generator


if __name__ == "__main__":

    timeline, prompt_generator = select_scenario(scenario_nr=2)
    commutePlanner = plan.CommutePlanner()

    app.run(host='0.0.0.0', debug=True)
