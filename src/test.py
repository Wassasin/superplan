import util
import data
import datetime
import geo
import config
import mock
import plan

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

# print g.directions("Sophiaweg 1", "St. Annastraat 1 Nijmegen", now)
# print g.resolve("Netherlands, Arnhem, Centraal Station")

plan.plan(tl, g)
