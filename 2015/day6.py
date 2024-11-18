'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def preprocess_data(data):
    lighting_instructions = []
    for d in data:
        d = d.replace("turn on", "on")
        d = d.replace("turn off", "off")
        d = d.replace(" through", "")
        instruction, start, end = d.split(" ")
        start = [int(i) for i in start.split(",")]
        end = [int(i) for i in end.split(",")]
        lighting_instructions.append([instruction, start, end])
    return lighting_instructions


def puzzle1(data):
    lighting_instructions = preprocess_data(data)
    lighting_configuration = \
        [[False for i in range(1000)] for j in range(1000)]

    for li in lighting_instructions:
        instruction = li[0]
        start_x, start_y = li[1]
        end_x, end_y = li[2]

        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                match instruction:
                    case "off":
                        lighting_configuration[x][y] = False
                    case "on":
                        lighting_configuration[x][y] = True
                    case "toggle":
                        lighting_configuration[x][y] = not lighting_configuration[x][y]

    print(
        f"The answer to puzzle 1 is: {sum(e for line in lighting_configuration for e in line if e)}")


def puzzle2(data):
    lighting_instructions = preprocess_data(data)
    lighting_configuration = \
        [[0 for i in range(1000)] for j in range(1000)]

    for li in lighting_instructions:
        instruction = li[0]
        start_x, start_y = li[1]
        end_x, end_y = li[2]

        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                match instruction:
                    case "off":
                        if lighting_configuration[x][y] == 0:
                            continue
                        lighting_configuration[x][y] -= 1
                    case "on":
                        lighting_configuration[x][y] += 1
                    case "toggle":
                        lighting_configuration[x][y] += 2

    print(
        f"The answer to puzzle 2 is: {sum(e for line in lighting_configuration for e in line if e)}")


puzzle1(data)
puzzle2(data)
