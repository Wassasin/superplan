import data
import datetime
import server.apis.weather as w

today = datetime.datetime.now().date()

timeline = data.Timeline()

timeline.append(data.Event(
        None,
        datetime.timedelta(hours=7.5),
        None,
        "sleep"
    ))
timeline.append(data.Event(
        None,
        datetime.timedelta(minutes=35),
        "Jadelaan 2, Utrecht",
        "morning routine"
    ))
timeline.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=8, minute=30)),
        datetime.timedelta(hours=2),
        "Agro Businesspark 99, Wageningen",
        "important business meeting"
    ))
timeline.append(data.Event(
        None,
        datetime.timedelta(minutes=15),
        None,
        "Coffee"
    ))
timeline.append(data.Event(
        datetime.datetime.combine(today, datetime.time(hour=14, minute=00)),
        datetime.timedelta(hours=1),
        "Agro Businesspark 99, Wageningen",
        "General work"
    ))


weather = w.WeatherResponse()