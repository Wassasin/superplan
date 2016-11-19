import requests
import datetime

from server.cache import Cache

class WeatherInt:
    def __init__(self, api):
        self.api = api

    def getFromSeries(self, latitude, longitude, time):
        series = self.api.get(latitude, longitude)["hourly"]["data"]
        for s in series:
            if time <= datetime.datetime.fromtimestamp(s["time"]) <= time + datetime.timedelta(hours=1):
                return s
        return None

    def mustScrapeCar(self, latitude, longitude, time):
        return self.getFromSeries(latitude, longitude, time)["temperature"] <= 0

    def isRaining(self, latitude, longitude, time):
        return self.getFromSeries(latitude, longitude, time)["precipProbability"] > 0.3

class WeatherAPI:
    def __init__(self, key):
        self.api_key = key
        self.cache = Cache('weather')

    def get(self, latitude, longitude):
        url_str = 'https://api.darksky.net/forecast/' + str(self.api_key) + '/'\
                 + str(latitude) + ',' + str(longitude)

        cache_key = 'lat' + str(latitude) + '_lon' + str(longitude)
        return self.cache.handle(
            cache_key,
            lambda: requests.get(url_str).json()
        )
