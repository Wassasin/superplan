import util
import data
import datetime

today = datetime.datetime.now().date()

events = []
events.append(data.Event(
        None,
        datetime.timedelta(hours=8),
        None,
        "sleep"
    ))
events.append(data.Event(
        None,
        datetime.timedelta(hours=1),
        None,
        "morning routine"
    ))
events.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=8, minute=30)),
        datetime.timedelta(hours=4),
        "Work, Nijmegen",
        "work"
    ))
events.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=12, minute=30)),
        datetime.timedelta(hours=1),
        "Work, Nijmegen",
        "meeting with Boss"
    ))
print util.isConflict(events)
