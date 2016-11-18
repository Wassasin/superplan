from enum import Enum

class Event:
    def __init__(self, startTime, duration, location, description):
        self.startTime = startTime
        self.duration = duration
        self.location = location
        self.description = description

class Timeline:
    def __init__(self, now):
        self.events = []
        self.now = now

class State:
    def __init__(self):
        self.gps = None
