import datetime

import config
import data
import mock
import plan
import util
from server.apis import geo
from server.apis import weather

today = mock.today
tl = mock.timeline
now = datetime.datetime.combine(today, datetime.time(hour=7, minute=0))
print 'conflict', util.isConflict(tl)

it = util.whatNow(tl, now)

currentEvent = it.current()
it.next()
nextEvent = it.current()

print 'current', currentEvent
print 'next', nextEvent

conf = config.Config()

g = geo.Geo(conf.get('google-key'))
cp = plan.CommutePlanner()

plan.plan(tl, g, cp)

w = weather.WeatherAPI(conf.get('darksky-key'))
lat, lng = g.resolve("Sint Annastraat 1")
wint = weather.WeatherInt(w)
print wint.mustScrapeCar(lat, lng, now)
print wint.isRaining(lat, lng, now)
