import util
import geo

def findCommutes(timeline, state, geo):
    pair = util.whatNow(timeline, state.now)

    e, it = pair


    loc = e.location

    try:
        while True:
            e = it.next()
            newLoc = e.location

            if loc is not None and newLoc is not None and loc != newLoc:
                print loc
                print newLoc
                print e.startTime
                d = geo.directions(loc, newLoc, e.startTime)
                print d
                yield d
                loc = newLoc
    except StopIteration:
        pass
