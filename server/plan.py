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

class CommutePlanner:
    def __init__(self, options=['walking', 'walking', 'bicycling', 'transit']):
        self.options = options

    def plan(self, a, b, arrival_time, g):
        fastest = None
        for o in self.options:
            l = g.directions(a, b, arrival_time, mode=o)[0]["legs"][0]
            duration = datetime.timedelta(seconds=l["duration"]["value"])
            if "departure_time" in l:
                startTime = datetime.datetime.fromtimestamp(l["departure_time"]["value"])
            else:
                startTime = arrival_time - duration

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
                startTime, duration, mode = cp.plan(it.current().location, s.location, s.now, g)
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
