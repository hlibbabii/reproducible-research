#!/usr/bin/env python3

import json

with open('test-data.csv', 'r') as f:
    input = f.readlines()

with open('model.pkl', 'r') as f:
    how_many = json.load(f)['n_layers']

with open('predictions.csv', 'w') as f:
    f.write('actual,predicted\n')
    for ind, actual in enumerate(input):
        actual = actual.rstrip('\n')
        predicted = 1 if ind < how_many else 0
        f.write(f"{actual},{predicted}\n")
