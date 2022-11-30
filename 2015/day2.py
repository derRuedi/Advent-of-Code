'''
    Advent of Code Day 2
    https://adventofcode.com/2015/day/2
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


# list of the dimensions (length l, width w, and height h)
# 2*l*w + 2*w*h + 2*h*l
square_feet = 0
ribbon = 0
for d in data:
    sides = [int(n) for n in d.split("x")]
    l, w, h = sides
    square_feet += 2*l*w + 2*w*h + 2*h*l
    square_feet += min(l*w, w*h, h*l)

    sides.sort()
    ribbon += 2*sides[0] + 2*sides[1] + (l*w*h)

print(f"Answer to puzzle 1: {square_feet}")
print(f"Answer to puzzle 2: {ribbon}")
