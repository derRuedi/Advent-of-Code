'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/11
'''

from copy import deepcopy

# input from website
from itertools import combinations
sample_input = False
input = 'day11_sample.txt' if sample_input else 'day11.txt'
with open(input, 'r') as f:
    image = [[x for x in y] for y in f.read().splitlines()]


def manhattan_distance(point_a, point_b):
    return abs(point_b[0] - point_a[0]) + abs(point_b[1] - point_a[1])


galaxies = [(x, y) for y, line in enumerate(image)
            for x, c in enumerate(line) if c == "#"]
pairs = list(combinations(galaxies, 2))
empty_rows = []
for idx, row in enumerate(image):
    if row.count(".") == len(row):
        empty_rows.append(idx)
empty_columns = []
for i in range(len(image[0])):
    if all(d == "." for d in [image[y][x] for y, line in enumerate(image) for x, c in enumerate(line) if x == i]):
        empty_columns.append(i)


for expansion in [None, 1_000_000]:
    distances = 0
    if expansion:
        space = expansion - 1
    else:
        space = 1
    for pair in pairs:
        lines_in_between = list(
            range(min(pair[0][1], pair[1][1])+1, max(pair[0][1], pair[1][1])))
        columns_in_between = list(
            range(min(pair[0][0], pair[1][0])+1, max(pair[0][0], pair[1][0])))

        add_x = 0
        for line_in_between in lines_in_between:
            if line_in_between in empty_rows:
                add_x += space

        add_y = 0
        for column_in_between in columns_in_between:
            if column_in_between in empty_columns:
                add_y += space

        distances += manhattan_distance(*pair) + add_x + add_y
    print(distances)
