'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/18
'''

import functools

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = [list(map(int, l.split(","))) for l in f.read().splitlines()]
    data.sort()

# checks = [
#     [-1, 0, 0],
#     [+1, 0, 0],
#     [0, -1, 0],
#     [0, +1, 0],
#     [0, 0, -1],
#     [0, 0, +1]
# ]

# total_sides = 0

# for point in data:
#     sides_per_point = 0
#     for c in checks:
#         neighbor = list(map(sum, zip(point, c)))
#         if neighbor not in data:
#             sides_per_point += 1
#     total_sides += sides_per_point

# print(total_sides)


with open(input, 'r') as f:
    cubes = {tuple(map(int, l.split(","))) for l in f.read().splitlines()}


def neighbors(x, y, z): return {
    (x+1, y, z),
    (x-1, y, z),
    (x, y+1, z),
    (x, y-1, z),
    (x, y, z+1),
    (x, y, z-1)
}


print(sum(neighbor not in cubes for point in cubes for neighbor in neighbors(*point)))
