import data
import datetime

def findFirstConcrete(timeline):
    it = timeline.begin()
    try:
        while True:
            it.next()
            if it.current().startTime is not None:
                return it
    except StopIteration:
        return None

def isConflict(timeline):
    it = findFirstConcrete(timeline)
    if it is None:
        return True

    now = it.current().startTime + it.current().duration
    try:
        while True:
            it.next()
            if it.current().startTime is not None:
                if now > it.current().startTime:
                    return True
                now = it.current().startTime
            now = now + it.current().duration
    except StopIteration:
        pass

    return False

def whatNow(timeline, now):
    it = findFirstConcrete(timeline)
    if it is None:
        return None

    time = it.current().startTime

    if now > time: # later then first fixed task
        if now < time + it.current().duration: # during first fixed task
            return it
        time += it.current().duration

        try:
            while True:
                it.next()
                if it.current().startTime is not None: # fixed task
                    if now < it.current().startTime: # before start
                        return it # free time, startTime has not yet occurred
                    time = it.current().startTime
                time += it.current().duration

                if now < time: # during this task
                    return it
        except StopIteration:
            pass
    else: # before first fixed task, calculate back?
        try:
            while True:
                it.prev()
                time -= it.current().duration
                if now >= time: # later then start of this task
                    return it
        except StopIteration:
            pass

    return None # free time, after everything else
