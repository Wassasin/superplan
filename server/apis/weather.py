import requests


from server.cache import Cache


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
