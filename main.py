#!/bin/python3
from DataProcesser import DataProcesser
from Model import Model
import json
from ProblemReport import ProblemReport


if __name__ == '__main__':
    dp = DataProcesser('data/prontos.json')

    model_input = dp.get_input()
    labels = dp.get_encoded_labels()

    model = Model(labels, model_input)

    test_pronto_files = ['data/test_pronto1.json', 'data/test_pronto2.json', 'data/test_pronto3.json']

    for test_pronto_file in test_pronto_files:
        with open(test_pronto_file, 'r') as testPronto:
            pronto = json.load(testPronto)
            problem_report = ProblemReport.from_dict(pronto)
            input = dp.process_pronto(problem_report)
            prediction = model.predict(input)
            predicted_label = dp.get_label(prediction)

            print(f'Predicted label for {test_pronto_file}: {predicted_label}')
