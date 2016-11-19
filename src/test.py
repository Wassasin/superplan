import util
import data
import datetime
import geo
import config

today = datetime.datetime.now().date()

tl = data.Timeline()

tl.append(data.Event(
        None,
        datetime.timedelta(hours=8),
        None,
        "sleep"
    ))
tl.append(data.Event(
        None,
        datetime.timedelta(hours=1),
        None,
        "morning routine"
    ))
tl.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=8, minute=30)),
        datetime.timedelta(hours=4),
        "Work, Nijmegen",
        "work"
    ))
tl.append(data.Event(
        None,
        datetime.timedelta(hours=1, minutes=0),
        None,
        "lunch"
    ))
tl.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=14, minute=00)),
        datetime.timedelta(hours=1),
        "Work, Nijmegen",
        "meeting with Boss"
    ))

print 'conflict', util.isConflict(tl)
s = data.State()

pair = util.whatNow(tl, datetime.datetime.combine(today, datetime.time(hour=7, minute=0)))

currentEvent, it = pair
nextEvent = it.next()

print 'current', currentEvent
print 'next', nextEvent

conf = config.Config()

g = geo.Geo(conf.get('google-key'))
print g.directions('St. Annastraat 1 Nijmegen', 'Sophiaweg 1 Nijmegen', nextEvent.startTime)
