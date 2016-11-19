import datetime

import config
import data
import mock
import util
from server.apis import geo
from server.apis import weather

today = mock.today
tl = mock.timeline

print 'conflict', util.isConflict(tl)
s = data.State()

pair = util.whatNow(tl, datetime.datetime.combine(today, datetime.time(hour=7, minute=0)))

currentEvent, it = pair
nextEvent = it.next()

print 'current', currentEvent
print 'next', nextEvent

conf = config.Config()

g = geo.Geo(conf.get('google-key'))
print g.directions('Jadelaan 2 Utrecht', 'MeteoGroup Wageningen', arrival=nextEvent.startTime, mode="driving")

w = weather.WeatherAPI(conf.get('darksky-key'))
w.get(50, 3)
