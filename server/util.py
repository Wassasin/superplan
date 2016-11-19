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


def findFirstConcrete(timeline):
    it = timeline.iter()
    try:
        while True:
            e = it.next()
            if e.startTime is not None:
                return (e, it)
    except StopIteration:
        return (None, None)


def isConflict(timeline):
    (first, it) = findFirstConcrete(timeline)
    if first is None:
        return True

    now = first.startTime + first.duration
    try:
        while True:
            e = it.next()
            if e.startTime is not None:
                if now > e.startTime:
                    return True
                now = e.startTime
            now = now + e.duration
    except StopIteration:
        pass

    return False


def whatNow(timeline, now):
    (first, it) = findFirstConcrete(timeline)
    if first is None:
        return True

    time = first.startTime

    if now > time: # later then first fixed task
        if now < time + first.duration: # during first fixed task
            return (first, it)
        time += first.duration

        try:
            while True:
                e = it.next()
                if e.startTime is not None:  # fixed task
                    if now < e.startTime:  # before start
                        it.prev()  # rewind, we've currently got free time
                        return (None, it)  # free time
                    time = e.startTime
                time += e.duration

                if now < time: # during this task
                    return (e, it)
        except StopIteration:
            pass
    else: # before first fixed task, calculate back?
        try:
            while True:
                e = it.prev()
                time -= e.duration
                if now >= time:  # later then start of this task
                    return (e, it)
        except StopIteration:
            pass

    return None  # free time, after everything else
