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

plan.plan(tl, g)

#w = weather.WeatherAPI(conf.get('darksky-key'))
#w.get(50, 3)