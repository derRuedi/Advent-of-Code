'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import re

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read()

row, column = map(int, re.findall(r"\d+", data))


nth_code = sum(range(1, column+1)) + sum(range(column, row + (column-1)))

print(nth_code)

a = 20151125
for i in range(1, nth_code):
    _, a = divmod(a*252533, 33554393)

print(a)
