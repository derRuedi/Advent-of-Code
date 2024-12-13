'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/8
'''

# input from website
from itertools import combinations
from collections import defaultdict
sample_input = False
input = 'day8_sample.txt' if sample_input else 'day8.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def generate_unique_lines(points):
    # generate all unique lines between a set of points.
    return list(combinations(points, 2))


def extend_line(point1, point2, steps=None, xmax=None, ymax=None):
    # extend the line between two points in both directions using whole numbers.
    x1, y1 = point1
    x2, y2 = point2

    # Calculate differences (direction vector)
    dx = x2 - x1
    dy = y2 - y1

    # new points
    points = []

    # Extend the line
    if steps:
        extended_point1 = (x1 - steps * dx, y1 - steps * dy)
        extended_point2 = (x2 + steps * dx, y2 + steps * dy)
        points.append(extended_point1)
        points.append(extended_point2)
        return points

    if xmax and ymax:
        steps = 1
        extended_point1 = (x1 - steps * dx, y1 - steps * dy)
        extended_point2 = (x2 + steps * dx, y2 + steps * dy)

        while 0 <= extended_point1[0] < xmax and 0 <= extended_point1[1] < ymax:
            points.append(extended_point1)
            steps += 1
            extended_point1 = (x1 - steps * dx, y1 - steps * dy)

        steps = 1
        while 0 <= extended_point2[0] < xmax and 0 <= extended_point2[1] < ymax:
            points.append(extended_point2)
            steps += 1
            extended_point2 = (x2 + steps * dx, y2 + steps * dy)

        return points

    return points


xmin, xmax = 0, len(data[0])
ymin, ymax = 0, len(data)

antennae = defaultdict(list)
for y in range(ymax):
    for x in range(xmax):
        if data[y][x] != ".":
            antennae[data[y][x]].append((x, y))


def calculate_antinodes(antennae, harmonics=False):
    unique_locations = set()
    for v in antennae.values():
        unique_lines = generate_unique_lines(v)
        for p1, p2 in unique_lines:
            if harmonics:
                antinodes = extend_line(p1, p2, xmax=xmax, ymax=ymax)
                for antinode in antinodes:
                    unique_locations.add(antinode)
            else:
                antinodes = extend_line(p1, p2, 1)
                for antinode in antinodes:
                    a_x, a_y = antinode
                    if xmin <= a_x < xmax and ymin <= a_y < ymax:
                        unique_locations.add(antinode)
        if harmonics:
            for a in v:
                unique_locations.add(a)
    return len(unique_locations)


print(f"puzzle 1: {calculate_antinodes(antennae)}")
print(f"puzzle 2: {calculate_antinodes(antennae, True)}")
