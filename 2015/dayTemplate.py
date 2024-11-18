'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def preprocess_data(data):
    pass


preprocess_data(data)
