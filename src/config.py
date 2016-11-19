import json
import os

class Config:
    def __init__(self):
        with open('./config.json', 'r') as infile:
            self.data = json.load(infile)

    def get(self, key):
        return self.data.get(key)
