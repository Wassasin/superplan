import util
import data
import datetime

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
        datetime.timedelta(hours=1, minutes=10),
        None,
        "lunch"
    ))
tl.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=13, minute=30)),
        datetime.timedelta(hours=1),
        "Work, Nijmegen",
        "meeting with Boss"
    ))

print 'conflict', util.isConflict(tl.events)
s = data.State()

pair = util.whatNow(tl, datetime.datetime.combine(today, datetime.time(hour=10, minute=0)))

currentEvent, it = pair
nextEvent = next(it)

print 'current', currentEvent
print 'next', nextEvent
