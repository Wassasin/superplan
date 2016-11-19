import data
import datetime
from datetime import time
import server.apis.weather as w

from data import Prompt

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


def prompt_generator(query_time):

    if time(hour=0) < query_time <= time(hour=5, minute=30):
        prompt = None
    elif time(hour=5, minute=30) < query_time:
        # TODO TdR 19/11/16: move to file.
        description = (
            "It was freezing last night, "
            "so I woke you up half an hour early "
            "to make sure you are on time. Hope "
            "you slept well. Prepare for a cold "
            "and sunny day: clear the ice of your "
            "windows and don't forget your gloves "
            "and sunglasses.",
        )
        today = datetime.datetime.now()
        new_time = datetime.datetime(today.year, today.month, today.day, query_time.hour, query_time.minute)
        prompt = Prompt(new_time, description, ["OK"])
    else:
        prompt = None
    return prompt
