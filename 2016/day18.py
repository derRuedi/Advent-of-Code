'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib
from copy import deepcopy

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read()

data = {(0, i): True if trap == "^" else False for i, trap in enumerate(data)}


def calculate_tiles(data, rows=40, print_room=False):
    tiles = len(data)

    for i in range(1, rows):
        for x in range(tiles):
            # A new tile is a trap only in one of the following situations:
            # - Its left and center tiles are traps, but its right tile is not.
            # - Its center and right tiles are traps, but its left tile is not.
            # - Only its left tile is a trap.
            # - Only its right tile is a trap.
            left = data[(i-1, x - 1)] if (i-1, x - 1) in data else False
            center = data[(i-1, x)]
            right = data[(i-1, x + 1)] if (i-1, x + 1) in data else False
            if (left and center and not right) or (center and right and not left) or (left and not center and not right) or (right and not center and not left):
                data[(i, x)] = True
            else:
                data[(i, x)] = False

    if print_room:
        for i in range(rows):
            for x in range(tiles):
                print("^" if data[(i, x)] else ".", end="")
            print()

    return data


def safe_tiles(data):
    print(sum((1 for d in data.values() if not d)))


safe_tiles(calculate_tiles(deepcopy(data), 40))
safe_tiles(calculate_tiles(deepcopy(data), 400000))
