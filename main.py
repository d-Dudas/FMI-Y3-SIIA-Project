#!/bin/python3
from DataProcesser import DataProcesser

if __name__ == '__main__':
    dp = DataProcesser('data/prontos.json')
    dp.process()
