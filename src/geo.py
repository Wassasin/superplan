import googlemaps

from cache import Cache


class Geo:
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)
        self.dirCache = Cache('geo-dir')
        self.resolveCache = Cache('geo-resolve')

    def resolve(self, loc):
        key = str(loc)
        return self.dirCache.handle(
            key,
            lambda: self.gmaps.geocode(loc))

    def directions(self, a, b, arrival=None, mode="transit"):
        key = ':'.join(map(str, [a, b, arrival, mode]))
        return self.dirCache.handle(
            key,
            lambda: self.gmaps.directions(
                a, b, mode=mode, arrival_time=arrival))
