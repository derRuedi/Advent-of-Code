'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/18
'''

# input from website
from shapely import Polygon
import re
sample_input = False
input = 'day18_sample.txt' if sample_input else 'day18.txt'
with open(input, 'r') as f:
    dig_plan = [[dir, int(meters), color[1:-1]]
                for line in f.read().splitlines()
                for dir, meters, color in [line.split(" ")]]


directions = {
    # Y, X
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}

lagoon = {}
current_position = (0, 0)

lagoon[current_position] = "#"

for dir, meters, color in dig_plan:
    for i in range(meters):
        current_position = (
            current_position[0] + directions[dir][0], current_position[1] + directions[dir][1])
        lagoon[current_position] = "#"

shape = Polygon(lagoon)
print(round(shape.area + (shape.length/2) + 1))
# is the same as the next line:
# coordinates are essentially the middle point of the square it lies in;
# this half a square area should be added around the border; buffer inflates the shapely polygon
# print(round(shape.buffer(.5, join_style='mitre').area))


lagoon = {}
current_position = (0, 0)
dir_color_mapping = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}

lagoon = []
lagoon.append(current_position)

for dir, meters, color in dig_plan:
    meters = int(color[1:-1], 16)
    dir = dir_color_mapping[int(color[-1])]

    current_position = (current_position[0] + directions[dir][0]
                        * meters, current_position[1] + directions[dir][1] * meters)
    lagoon.append(current_position)

shape = Polygon(lagoon)
print(round(shape.area + (shape.length/2) + 1))
# is the same as the next line:
# coordinates are essentially the middle point of the square it lies in;
# this half a square area should be added around the border; buffer inflates the shapely polygon
# print(round(shape.buffer(.5, join_style='mitre').area))
