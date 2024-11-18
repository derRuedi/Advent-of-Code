'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib
import re

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]


num_valid_triangles = 0
for line in data:
    a, b, c = line
    if a + b > c and a + c > b and b + c > a:
        num_valid_triangles += 1

print("part 1:", num_valid_triangles)


num_valid_triangles = 0
for j in range(3):
    for i in range(0, len(data), 3):
        a = data[i][j]
        b = data[i+1][j]
        c = data[i+2][j]
        if a + b > c and a + c > b and b + c > a:
            num_valid_triangles += 1

print("part 2:", num_valid_triangles)
