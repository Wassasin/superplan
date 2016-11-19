import datetime

from server import data, util
from server.apis import geo

def spoolRevToFixed(it):
    try:
        while True:
            it.prev()
            if it.current().startTime is not None:
                return it
    except StopIteration:
        return None

class commutePlanner:
    def __init__(self, options=['walking', 'walking', 'bicycling', 'transit']):
        self.options = options

    def plan(self, g, a, b, arrival_time):
        fastest = None
        for o in options:
            l = g.directions(it.current().location, s.location, s.now, mode=o)[0]["legs"][0]
            duration = datetime.timedelta(seconds=l["duration"]["value"])
            startTime = datetime.datetime.fromtimestamp(l["departure_time"]["value"])
            if fastest is None or duration < fastest[1]:
                fastest = (startTime, duration, o)

        return fastest


def plan(timeline, g, cp):
    # we plan backwards
    it = spoolRevToFixed(timeline.end())
    if it is None:
        return timeline

    s = data.State(it.current())

    newEvents = []
    try:
        while True:
            it.prev()
            if it.current().location is not None and s.location != it.current().location:
                startTime, duration, mode = cp.plan(it.current().location, s.location, s.now)
                e = data.Event(startTime, duration, it.current().location, "commute by "+mode)
                s.updateRev(e)
                newEvents.append(e)

            e = it.current()
            s.updateRev(e)
            e.startTime = s.now
            e.location = s.location
            newEvents.append(e)

    except StopIteration:
        pass

    return data.Timeline(reversed(newEvents))
