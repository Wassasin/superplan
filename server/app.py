from __future__ import print_function
from flask import Flask, jsonify, request
import sys
import datetime
from server import config, plan
from server.apis import geo

# Mocking for demo
from server import (
    mock, mock_scenario2
)

global timeline
timeline = None

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


@app.route("/schedule")
def getSchedule():
    conf = config.Config()
    g = geo.Geo(conf.get('google-key'))
    events = map(object_to_dict, plan.plan(timeline, g, commutePlanner).events)
    return jsonify(events=events)


@app.route("/prompts")
def getPrompts(time=None):
    if time is not None:
        # Do mocking.
        pass
    else:
        # Don't do mocking.
        pass

    prompts = []
    return jsonify(prompts=prompts)


@app.route("/resolve/<int:eventId>/cancel", methods=["POST"])
def resolveCancel(eventId):
    return jsonify(action="resolveCancel", eventId=eventId)


@app.route("/resolve/<int:eventId>/move", methods=["POST"])
def resolveMove(eventId):
    newTime = request.json["newTime"]
    return jsonify(action="resolveMove", eventId=eventId, newTime=newTime)


def select_scenario(scenario_nr=0):
    if scenario_nr == 0:
        return mock.timeline
    if scenario_nr == 1:
        raise NotImplementedError
    if scenario_nr == 2:
        return mock_scenario2.timeline


if __name__ == "__main__":
    timeline = select_scenario(scenario_nr=2)
    commutePlanner = plan.CommutePlanner()

    app.run(host='0.0.0.0', debug=True)
