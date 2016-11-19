import data
import datetime

today = datetime.datetime.now().date()

timeline = data.Timeline()

timeline.append(data.Event(
        None,
        datetime.timedelta(hours=8),
        None,
        "sleep"
    ))
timeline.append(data.Event(
        None,
        datetime.timedelta(hours=1),
        None,
        "morning routine"
    ))
timeline.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=8, minute=30)),
        datetime.timedelta(hours=4),
        "Work, Nijmegen",
        "work"
    ))
timeline.append(data.Event(
        None,
        datetime.timedelta(hours=1, minutes=0),
        None,
        "lunch"
    ))
timeline.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=14, minute=00)),
        datetime.timedelta(hours=1),
        "Work, Nijmegen",
        "meeting with Boss"
    ))