'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/14
'''

from copy import deepcopy
from icecream import ic

# input from website
sample_input = False
input = 'day14_sample.txt' if sample_input else 'day14.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def tilt(matrix):
    new_data = []
    for line in matrix:
        new_line = "#".join([('O'*l.count('O')).ljust(len(l), '.')
                            for l in line.split("#")])
        new_data.append(new_line)
    return new_data


def cycle(matrix):
    matrix = list(map("".join, zip(*matrix)))
    for i in range(3):
        matrix = tilt(matrix)
        matrix = list(map("".join, zip(*matrix)))[::-1]
    matrix = tilt(matrix)
    return [c[::-1] for c in matrix]


def calculate_total_load(matrix):
    return sum([sum([i+1 for i, l in enumerate(line[::-1]) if l == "O"]) for line in matrix])


def part1(matrix):
    matrix = list(map("".join, zip(*matrix)))
    matrix = tilt(matrix)
    return calculate_total_load(matrix)


def part2(data):
    x = data
    total_cycles = 1_000_000_000
    cycleresults = []
    for i in range(total_cycles):
        x = cycle(x)
        if x in cycleresults:
            cycle_length = len(cycleresults) - cycleresults.index(x)
            cycle_start = cycleresults.index(x)
            break
        else:
            cycleresults.append(x)

    res = ((total_cycles - cycle_start) % cycle_length) + cycle_start
    z = data
    for i in range(res):
        z = cycle(z)
    return calculate_total_load(list(map("".join, zip(*z))))


for i in [part1(data), part2(data)]:
    print(i)
