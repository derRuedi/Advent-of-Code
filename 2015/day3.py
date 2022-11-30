'''
    Advent of Code Day 3
    https://adventofcode.com/2015/day/3
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read()


def traverse(data):
    x = 0
    y = 0
    houses = {}
    houses[f"{x}:{y}"] = 1

    for d in data:
        match d:
            case "^":
                y += 1
            case "v":
                y -= 1
            case "<":
                x += 1
            case ">":
                x -= 1
        if f"{x}:{y}" in houses.keys():
            houses[f"{x}:{y}"] += 1
        else:
            houses[f"{x}:{y}"] = 1
    return houses


def puzzle1(data):
    houses = traverse(data)
    print(
        f"The answer to puzzle 1 is: {sum(1 for k, v in houses.items() if v >= 1)}")


def puzzle2(data):
    santa_data = data[0::2]
    robot_data = data[1::2]

    santa_houses = traverse(santa_data)
    robot_houses = traverse(robot_data)

    houses_visited = {}

    for houses in [santa_houses, robot_houses]:
        for k, v in houses.items():
            if k in houses_visited.keys():
                houses_visited[k] += v
            else:
                houses_visited[k] = v

    print(
        f"The answer to puzzle 2 is: {sum(1 for k, v in houses_visited.items() if v >= 1)}")


puzzle1(data)
puzzle2(data)
