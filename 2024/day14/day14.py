'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/14
'''
from collections import defaultdict
import re
import time
from termcolor import colored

# input from website
sample_input = False
input = 'day14_sample.txt' if sample_input else 'day14.txt'
with open(input, 'r') as f:
    data = [list(map(int, re.findall(r"-?\d+", line)))
            for line in f.read().splitlines()]


if sample_input:
    x_min, x_max = 0, 11
    y_min, y_max = 0, 7
else:
    x_min, x_max = 0, 101
    y_min, y_max = 0, 103


def print_robot_space(robot_positions, highlight_points=None):
    print()

    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            if highlight_points and (x, y) in highlight_points:
                print(colored(robot_positions.get((x, y), "."),
                      "red", attrs=["bold"]), end="")
            else:
                print(robot_positions.get((x, y), "."), end="")
        print()
    print()


robots = {}
for idx, robot in enumerate(data):
    robots[idx] = {
        "p": (robot[0], robot[1]),
        "v": (robot[2], robot[3]),
        "cp": (robot[0], robot[1]),
    }

for seconds in range(101):
    for k in robots.keys():
        robots[k]["cp"] = ((robots[k]["p"][0] + seconds * robots[k]["v"][0]) % x_max,
                           (robots[k]["p"][1] + seconds * robots[k]["v"][1]) % y_max)

robot_positions = defaultdict(int)
highlight_points = [r["cp"] for r in robots.values()]
for hp in highlight_points:
    robot_positions[hp] += 1
print_robot_space(robot_positions, highlight_points)
print()


def in_quadrant_range(x, y, quadrant=1):
    if quadrant == 1:
        return (0 <= x < x_max // 2 and 0 <= y < y_max // 2)
    elif quadrant == 2:
        return (x_max // 2 < x <= x_max and 0 <= y < y_max // 2)
    elif quadrant == 3:
        return (0 <= x < x_max // 2 and y_max // 2 < y <= y_max)
    elif quadrant == 4:
        return (x_max // 2 < x <= x_max and y_max // 2 < y <= y_max)
    else:
        print("whoops")
        exit(-1)


def calculate_robots_in_quadrant(robot_positions, quadrant=1):
    return sum([
        robot_positions.get((x, y), 0) for x in range(x_max) for y in range(y_max) if in_quadrant_range(x, y, quadrant)
    ])


def calculate_robots_in_quadrants(robot_positions):
    return calculate_robots_in_quadrant(robot_positions, 1) * \
        calculate_robots_in_quadrant(robot_positions, 2) * \
        calculate_robots_in_quadrant(robot_positions, 3) * \
        calculate_robots_in_quadrant(robot_positions, 4)


print(calculate_robots_in_quadrants(robot_positions))


# //////// part 2
# reset

robots = {}
for idx, robot in enumerate(data):
    robots[idx] = {
        "p": (robot[0], robot[1]),
        "v": (robot[2], robot[3]),
        "cp": (robot[0], robot[1]),
    }


seconds = 0
while True:
    for k in robots.keys():
        robots[k]["cp"] = ((robots[k]["p"][0] + seconds * robots[k]["v"][0]) %
                           x_max, (robots[k]["p"][1] + seconds * robots[k]["v"][1]) % y_max)
    robot_positions = defaultdict(int)
    highlight_points = [r["cp"] for r in robots.values()]
    for hp in highlight_points:
        robot_positions[hp] += 1
    if len(highlight_points) == len(robot_positions):
        break
    seconds += 1

print_robot_space(robot_positions, highlight_points)
print(seconds)
