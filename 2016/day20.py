'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = [[int(a) for a in line.split("-")]
            for line in f.read().splitlines()]


data.sort()

lower = data[0][1]
upper = data[-1][1]

allowed_ips = []

while lower < upper:
    for line in data:
        if line[0] <= lower + 1 <= line[1] - 1:
            lower = line[1]
    lower += 1
    allowed_ips.append(lower)

print(f"Answer to puzzle #1 is: {allowed_ips[0]}")
print(f"Answer to puzzle #2 is: {len(allowed_ips)-1}")
