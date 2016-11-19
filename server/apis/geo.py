import googlemaps

from server.cache import Cache


class Geo:
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)
        self.cache = Cache('geo')

    def directions(self, a, b, arrival=None, mode=["transit", "driving"]):
        key = '-'.join(map(str, [a, b, arrival, mode]))
        return self.cache.handle(
            key,
            lambda: self.gmaps.directions(
                a, b, mode=mode, arrival_time=arrival))
