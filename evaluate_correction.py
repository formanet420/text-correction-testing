#!/usr/bin/python3

import argparse
from Levenshtein import distance

# pokud import selhal, je to kvůli tomu, že musíte nainstalovat
# závislosti. Spusťe v terminálu z této složky příkaz pip3 install -r requirements.txt

def read_file(path):
    with open(path, 'r') as input_file:
        string = input_file.read()
        return string

def evaluate(reference, evaluated):
    print('computing levenshtein distance...')
    errors_count = distance(reference, evaluated)
    print(f'Errors: {errors_count}')

parser = argparse.ArgumentParser()
parser.add_argument('reference')
parser.add_argument('evaluated')
args = parser.parse_args()

reference = read_file(args.reference)
evaluated = read_file(args.evaluated)

evaluate(reference, evaluated)
