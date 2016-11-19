import util
import data
import datetime
import geo
import config
import mock

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
print g.directions('St. Annastraat 1 Nijmegen', 'Sophiaweg 1 Nijmegen', nextEvent.startTime)
