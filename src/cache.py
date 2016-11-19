import json
import os

class Cache:
    def __init__(self, name):
        self.path = './cache/cache-'+name+'.json'
        self.data = {}

        if os.path.exists(self.path):
            self.load()

    def load(self):
        with open(self.path, 'r') as infile:
            self.data = json.load(infile)

    def save(self):
        with open(self.path, 'w') as outfile:
            json.dump(self.data, outfile)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def get(self, key):
        return self.data.get(key)

    def handle(self, key, f):
        result = self.get(key)
        if result is not None:
            return result

        result = f()
        self.set(key, result)
        return result
