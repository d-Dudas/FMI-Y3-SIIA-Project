#!/bin/python3
from DataProcesser import DataProcesser
from Model import Model

if __name__ == '__main__':
    dp = DataProcesser('data/prontos.json')

    model_input = dp.get_input()
    labels = dp.get_encoded_labels()

    model = Model(labels, model_input)
