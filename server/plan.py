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
    def __init__(self, wint, options=['walking', 'driving', 'bicycling', 'transit']):
        self.wint = wint
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

            a_lat, a_lng = g.resolve(a)
            b_lat, b_lng = g.resolve(b)

            descr = o

            if o == 'walking':
                if self.wint.isRaining(a_lat, a_lng, startTime):
                    descr += " (bring umbrella)"

            if o == 'driving':
                if self.wint.mustScrapeCar(a_lat, a_lng, startTime):
                    duration += datetime.timedelta(minutes=5)
                    descr += " (car needs scraping)"

            if fastest is None or duration < fastest.duration:
                fastest = data.Event(startTime, duration, a, "commute by "+descr)

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
                e = cp.plan(it.current().location, s.location, s.now, g)
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
