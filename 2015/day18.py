'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = [list(i) for i in f.read().splitlines()]


points = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def animate(data, corner_lights_on=False, times=100):
    if corner_lights_on:
        data[0][0] = "#"
        data[0][len(data[0])-1] = "#"
        data[len(data)-1][0] = "#"
        data[len(data)-1][len(data[0])-1] = "#"

    for i in range(times):
        new_data = [['.' for x in range(len(data))]
                    for y in range(len(data[0]))]
        if corner_lights_on:
            new_data[0][0] = "#"
            new_data[0][len(data[0])-1] = "#"
            new_data[len(data)-1][0] = "#"
            new_data[len(data)-1][len(data[0])-1] = "#"
        for y in range(len(data)):
            for x in range(len(data[y])):
                no_of_on_neighbors = 0
                for p in points:
                    if x + p[0] < 0 or x + p[0] >= len(data[y]) or y + p[1] < 0 or y + p[1] >= len(data):
                        continue
                    else:
                        if data[y + p[1]][x + p[0]] == "#":
                            no_of_on_neighbors += 1
                if data[y][x] == "#" and (no_of_on_neighbors == 2 or no_of_on_neighbors == 3):
                    new_data[y][x] = "#"
                elif data[y][x] == "." and no_of_on_neighbors == 3:
                    new_data[y][x] = "#"
        data = new_data

    print(sum([i.count("#") for i in data]))


# animate(data)
# animate(data, True)


# trying the same with sets instead of lists:

part2 = True
if part2:
    corners = {(0, 0), (99, 99), (0, 99), (99, 0)}
else:
    corners = set()

with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    lights = corners | {(x, y) for y, line in enumerate(f)
                        for x, char in enumerate(line) if char == "#"}


def neighbors(x, y): return sum((_x, _y) in lights for _x in (x-1, x, x+1)
                                for _y in (y-1, y, y+1) if (_x, _y) != (x, y))


for i in range(100):
    lights = corners | {(x, y) for y in range(100) for x in range(100)
                        if ((x, y) in lights and (neighbors(x, y) == 2 or neighbors(x, y) == 3)) or
                        ((x, y) not in lights and neighbors(x, y) == 3)}

print(len(lights))
