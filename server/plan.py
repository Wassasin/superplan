import data
import util
import geo
import datetime

def spoolRevToFixed(it):
    try:
        while True:
            it.prev()
            if it.current().startTime is not None:
                return it
    except StopIteration:
        return None

def plan(timeline, g):
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
                l = g.directions(it.current().location, s.location, s.now)[0]["legs"][0]
                duration = datetime.timedelta(seconds=l["duration"]["value"])
                startTime = datetime.datetime.fromtimestamp(l["departure_time"]["value"])
                e = data.Event(startTime, duration, it.current().location, "Commute")
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
