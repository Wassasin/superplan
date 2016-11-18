import data

#fromCalendar -> Event[]
# getLocal -> Event[]
# merge all events from sources

# getTravelTime(a, b, mode) -> duration
# if duration > timeLeft:
#   push message "you're late"
# else
#   do nothing

import datetime

def findFirstConcrete(events):
    it = iter(events)
    try:
        while True:
            e = next(it)
            if e.startTime is not None:
                return (e, it)
    except StopIteration:
        return (None, None)

def isConflict(events):
    if len(events) == 0:
        return True

    (first, it) = findFirstConcrete(events)
    if first is None:
        return True

    now = first.startTime + first.duration
    try:
        while True:
            e = next(it)
            if e.startTime is not None:
                if now > e.startTime:
                    return True
                now = e.startTime
            now = now + e.duration
    except StopIteration:
        pass

    return False
