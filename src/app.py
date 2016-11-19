from __future__ import print_function
import sys
from flask import Flask, jsonify, request

app = Flask("superplan")

@app.route("/")
def root():
    return jsonify(msg="Welcome! See https://github.com/Wassasin/superplan for my interface.")

@app.route("/schedule")
def getSchedule():
    events = []

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
    app.run(debug=True)
