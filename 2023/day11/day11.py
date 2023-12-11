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

image2 = deepcopy(image)


def apply_gravitational_effects(matrix):
    blank_lines = []
    for idx, line in enumerate(matrix):
        if line.count(".") == len(line):
            blank_lines.append(idx)

    for line_number in blank_lines[::-1]:
        matrix.insert(line_number, matrix[line_number][:])

    transposed_matrix = list(zip(*matrix))
    blank_columns = []
    for idy, column in enumerate(transposed_matrix):
        if column.count(".") == len(column):
            blank_columns.append(idy)

    for column_number in blank_columns[::-1]:
        transposed_matrix.insert(
            column_number, transposed_matrix[column_number][:])

    matrix = list(map(list, zip(*transposed_matrix)))
    return matrix


def manhattan_distance(point_a, point_b):
    return abs(point_b[0] - point_a[0]) + abs(point_b[1] - point_a[1])


image = apply_gravitational_effects(image)
galaxies = [(x, y) for y, line in enumerate(image)
            for x, c in enumerate(line) if c == "#"]

pairs = list(combinations(galaxies, 2))
distances = sum([manhattan_distance(a, b) for a, b in pairs])
print(distances)

# --------
# different approach for puzzle 2

# galaxies = [(x, y) for y, line in enumerate(image2)
#             for x, c in enumerate(line) if c == "#"]
# pairs = list(combinations(galaxies, 2))


# distances = 0
# space = 1_000_000 - 1
# print(len(pairs))
# for idx, pair in enumerate(pairs):

#     if idx % 1000 == 0:
#         print(f"{idx} / {len(pairs)}")

#     lines_in_between = list(
#         range(min(pair[0][1], pair[1][1])+1, max(pair[0][1], pair[1][1])))
#     columns_in_between = list(
#         range(min(pair[0][0], pair[1][0])+1, max(pair[0][0], pair[1][0])))

#     add_x = 0
#     for line_in_between in lines_in_between:
#         if image2[line_in_between].count(".") == len(image2[line_in_between]):
#             add_x += space

#     add_y = 0
#     for column_in_between in columns_in_between:
#         if all(d == "." for d in [image2[y][x] for y, line in enumerate(image2) for x, c in enumerate(line) if x == column_in_between]):
#             add_y += space

#     distances += manhattan_distance(*pair) + add_x + add_y

# print(distances)


# --------
# different approach for puzzle 2

galaxies = [(x, y) for y, line in enumerate(image2)
            for x, c in enumerate(line) if c == "#"]
pairs = list(combinations(galaxies, 2))


empty_rows = []
for idx, row in enumerate(image2):
    if row.count(".") == len(row):
        empty_rows.append(idx)

empty_columns = []
for i in range(len(image2[0])):
    if all(d == "." for d in [image2[y][x] for y, line in enumerate(image2) for x, c in enumerate(line) if x == i]):
        empty_columns.append(i)


distances = 0
space = 1_000_000 - 1
print(len(pairs))
for idx, pair in enumerate(pairs):
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
