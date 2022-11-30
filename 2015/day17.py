'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper
from itertools import combinations

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = list(map(int, f.read().splitlines()))


def puzzle1(data):
    # # solution with for loop
    # solutions = 0
    # for i in range(1, len(data)):
    #     solutions += len([1 for c in combinations(data, i) if sum(c) == 150])
    # print(solutions)

    # # solution with list comprehension
    print(len([c for i in range(1, len(data))
          for c in combinations(data, i) if sum(c) == 150]))


def puzzle2(data):
    container_combinations = [c for i in range(
        1, len(data)) for c in combinations(data, i) if sum(c) == 150]
    minimum_length = len(min(container_combinations, key=lambda x: len(x)))
    print(len([c for c in container_combinations if len(c) == minimum_length]))

    # # or as one long line
    # print(len([c for c in container_combinations if len(c) == len(
    #     min(container_combinations, key=lambda x: len(x)))]))


puzzle1(data)
puzzle2(data)
