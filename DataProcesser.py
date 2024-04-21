#!/bin/python3

import json

class DataProcesser:
    def __init__(self, dataFile):
        self.dataFile = dataFile

    def process(self):
        with open(self.dataFile, 'r') as file:
            prontos = json.load(file)['values']
            print(len(prontos))
