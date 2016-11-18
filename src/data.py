import datetime

class Event:
    def __init__(self, startTime, duration, location, description, participants=[]):
        self.startTime = startTime
        self.duration = duration
        self.location = location
        self.description = description
        self.participants = participants

    def __str__(self):
        params = [self.startTime, self.duration, self.location, self.description]
        return ' '.join(map(str, filter(lambda x: x is not None, params)))

class Timeline:
    def __init__(self):
        self.events = []

    def append(self, e):
        self.events.append(e)

class State:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.location = None
