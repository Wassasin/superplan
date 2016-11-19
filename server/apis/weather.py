import datetime
import requests

class Weather:
    def __init__(self,key):
        self.apikey = key
        pass

    def get(self, latitude, longitude):
        urlstr = 'https://api.darksky.net/forecast/'+str(apikey)+'/'+str(latitude)+','+str(longitude)
        print urlstr
        r = requests.get(urlstr)
        print r.status_code
        print r.json()

    def is_freezing(self, latitude, longitude):
        pass

w = Weather()
w.get(52.094476, 5.106866)
