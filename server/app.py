from __future__ import print_function
from flask import Flask, jsonify, request
import sys
import datetime
import mock

def debug(obj):
    print(obj, file=sys.stderr)

app = Flask("superplan")

timeline = mock.timeline


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
    events = map(object_to_dict, timeline.events)
    return jsonify(events=events)


@app.route("/prompts")
def getPrompts():
    prompts = []
    return jsonify(prompts=prompts)


@app.route("/resolve/<int:eventId>/cancel", methods=["POST"])
def resolveCancel(eventId):
    return jsonify(action="resolveCancel", eventId=eventId)


@app.route("/resolve/<int:eventId>/move", methods=["POST"])
def resolveMove(eventId):
    newTime = request.json["newTime"]
    return jsonify(action="resolveMove", eventId=eventId, newTime=newTime)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
