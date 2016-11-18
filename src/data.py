import datetime

class Event:
    def __init__(self, startTime, duration, location, description, participants=[]):
        self.startTime = startTime
        self.duration = duration
        self.location = location
        self.description = description
        self.participants = participants

    def __str__(self):
        result = ''
        if self.startTime is None:
            result += 'Fluid '
        else:
            result += 'Fixed '
            result += str(self.startTime) + ' to ' + str(self.startTime + self.duration) + ' '

        result += '(' + str(self.duration) + ') '
        result += '@ ' + str(self.location) + ' '
        result += self.description
        return result

class Timeline:
    def __init__(self):
        self.events = []

    def append(self, e):
        self.events.append(e)

class State:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.location = None
