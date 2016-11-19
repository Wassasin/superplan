import googlemaps
from datetime import datetime
from cache import Cache

class Geo:
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)
        self.cache = Cache('geo')

    def directions(self, a, b, arrival):
        key = '-'.join(map(str, [a, b, arrival]))
        return self.cache.handle(key, lambda: self.gmaps.directions(a, b, mode="transit", arrival_time=arrival))
