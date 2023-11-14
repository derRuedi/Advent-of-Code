'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/5
'''
from icecream import ic

# input from website
sample_input = False
input = 'day5_sample.txt' if sample_input else 'day5.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def puzzle1(data):
    instructions = {key: int(value) for key, value in enumerate(data)}
    steps = 0
    position = 0
    while position in instructions:
        steps += 1
        step = instructions[position]
        instructions[position] += 1
        position += step

    return steps


def puzzle2(data):
    instructions = {key: int(value) for key, value in enumerate(data)}
    steps = 0
    position = 0
    while position in instructions:
        steps += 1
        step = instructions[position]
        if step >= 3:
            instructions[position] -= 1
        else:
            instructions[position] += 1
        position += step

    return steps


print(puzzle1(data))
print(puzzle2(data))
