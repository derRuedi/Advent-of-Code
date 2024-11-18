'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib
from collections import defaultdict

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    instructions = [(k[0], int(k[1:])) for k in f.read().split(", ")]

direction = "N"
position = defaultdict(int)
visited_locations = set()
visited_location_twice = False


def change_direction(cur_direction, turn):
    #       N
    #   W       O
    #       S
    directions = ["N", "O", "S", "W"]
    cur_direction_index = directions.index(cur_direction)
    if turn == "L":
        new_direction_index = cur_direction_index - 1
    else:
        new_direction_index = (cur_direction_index + 1) % len(directions)

    return directions[new_direction_index]


for turn, distance in instructions:
    direction = change_direction(direction, turn)
    for i in range(distance):
        match direction:
            case "N":
                position["y"] += 1
            case "O":
                position["x"] += 1
            case "S":
                position["y"] -= 1
            case "W":
                position["x"] -= 1
        cur_position = (position["x"], position["y"])
        if not visited_location_twice:
            if cur_position not in visited_locations:
                visited_locations.add(cur_position)
            else:
                print(
                    f"Answer to puzzle 2: {sum(abs(i) for i in cur_position)}")
                visited_location_twice = True

print(f"Answer to puzzle 1: {sum(abs(i) for i in position.values())}")
