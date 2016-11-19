import datetime


class Event:
    def __init__(
            self, start_time, duration, location, description, participants=[]):
        self.startTime = start_time
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
            result += str(self.startTime) + ' to ' + \
                      str(self.startTime + self.duration) + ' '

        result += '(' + str(self.duration) + ') '
        result += '@ ' + str(self.location) + ' '
        result += self.description
        return result


class BiIterator:
    def __init__(self, subject, i = -1):
        self.i = i
        self.subject = subject

    def next(self):
        if self.i >= len(self.subject)-1:
            raise StopIteration

        self.i += 1

    def prev(self):
        if self.i <= 0:
            raise StopIteration

        self.i -= 1

    def current(self):
        return self.subject[self.i]


class Timeline:

    def __init__(self, events=[]):
        self.events = list(events)

    def __len__(self):
        return len(self.events)

    def __getitem__(self, i):
        return self.events[i]

    def append(self, e):
        self.events.append(e)

    def begin(self):
        return BiIterator(self, -1)

    def end(self):
        return BiIterator(self, len(self.events))


class State:
    def __init__(self, event): # fixed event, with location
        self.now = event.startTime
        self.location = event.location

    def updateRev(self, event):
        if event.startTime is not None:
            self.now = event.startTime
        else:
            self.now -= event.duration

        if event.location is not None:
            self.location = event.location


class Prompt:

    def __init__(self, time, description, answers):
        self.time = time
        self.description = description
        self.answers = answers
