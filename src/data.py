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
    def __init__(self, subject):
        self.i = 0
        self.subject = subject

    def next(self):
        if self.i >= len(self.subject)-1:
            raise StopIteration

        self.i += 1
        return self.current()

    def prev(self):
        if self.i <= 0:
            raise StopIteration

        self.i -= 1
        return self.current()

    def current(self):
        return self.subject[self.i]


class Timeline:

    def __init__(self):
        self.events = []

    def __len__(self):
        return len(self.events)

    def __getitem__(self, i):
        return self.events[i]

    def append(self, e):
        self.events.append(e)

    def iter(self):
        return BiIterator(self)


class State:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.location = None
