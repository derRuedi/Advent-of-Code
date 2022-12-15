'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/15
'''

import re
from termcolor import colored

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

pattern = re.compile(r"(-?\d+)")
data = [list(map(int, pattern.findall(line))) for line in data]

# sensors, beacons and distance
sbd = []
x_values = []
y_values = []

for line in data:
    sbd.append(
        {
            "sensor": (line[0], line[1]),
            "beacon": (line[2], line[3]),
            "distance": abs(line[0] - line[2]) + abs(line[1] - line[3])
        }
    )
    x_values.append(sbd[-1]["sensor"][0] - sbd[-1]["distance"])
    x_values.append(sbd[-1]["sensor"][0] + sbd[-1]["distance"])
    y_values.append(sbd[-1]["sensor"][1] - sbd[-1]["distance"])
    y_values.append(sbd[-1]["sensor"][1] + sbd[-1]["distance"])

min_x = min(x_values)
max_x = max(x_values)

min_y = min(y_values)
max_y = max(y_values)

x_offset = abs(min_x)
y_offset = abs(min_y)

print("min_x", min_x)
print("max_x", max_x)

print("min_y", min_y)
print("max_y", max_y)

# initialize matrix
matrix = [["." for x in range(max_x - min_x + 1)]
          for y in range(max_y - min_y + 1)]


def print_matrix(matrix):
    print()
    # header row
    spacer = " "
    print(
        f"\t{spacer.join([' ' if l % 5 != 0 else str(l)[-1] for l in range(min_x, max_x)])}")

    # actual matrix
    for i, line in enumerate(matrix):
        print(
            f"{i+min_y}\t{spacer.join([l if l in ['.', '#'] else colored(l, 'red', attrs=['bold'])for l in line])}")
    print()


for line in sbd:
    print(line)
    matrix[line["sensor"][1] + y_offset][line["sensor"][0] + x_offset] = "S"
    matrix[line["beacon"][1] + y_offset][line["beacon"][0] + x_offset] = "B"

    #line = sbd[6]

    distance = line["distance"]
    for y in range(-distance, distance+1):
        for x in range(-distance, distance+1):
            if abs(x)+abs(y) <= distance and matrix[y+y_offset+line["sensor"][1]][x+x_offset+line["sensor"][0]] == ".":
                matrix[y+y_offset+line["sensor"][1]][x +
                                                     x_offset+line["sensor"][0]] = "#"


print_matrix(matrix)

print(matrix[2000000+y_offset].count("#"))
