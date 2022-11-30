import itertools
from timeit import default_timer as timer
'''
Advent of Code Day 2
https://adventofcode.com/2017/day/2
'''

# input from website in raw format

with open('day2.input.txt', 'r') as f:
    data = f.read().splitlines()


def puzzle1(data):
    data = [line.split("\t") for line in data]

    diff = 0
    for line in data:
        line = [int(num) for num in line]
        diff += max(line) - min(line)
    print(f"Result of Puzzle 1 is: {diff}.")


def puzzle2(data):
    data = [line.split("\t") for line in data]

    diff = 0
    for line in data:
        line = [int(num) for num in line]

        sol = 0
        for i in range(len(line)):
            for j in range(len(line[i+1:])):
                if line[i] % line[i+j+1] == 0:
                    # print(f"sol = line[i] / line[i+j] = line[{i}] / line[{i}+{j+1}] = {line[i]} / {line[i+j+1]} = {line[i] / line[i+j+1]}")
                    sol = line[i] / line[i+j+1]
                    break
                elif line[i+j+1] % line[i] == 0:
                    # print(f"sol = line[i+j] / line[i] = line[{i} + {j+1}] / line[{i}] = {line[i+j+1]} / {line[i]} = {line[i+j+1] / line[i]}")
                    sol = line[i+j+1] / line[i]
                    break
        diff += int(sol)

    print(f"Result of Puzzle 2 is: {diff}.")


def puzzle2_smarter(data):
    data = [line.split("\t") for line in data]

    diff = 0
    for line in data:
        line = [int(num) for num in line]

        for i, j in itertools.product(line, line):
            if i == j:
                continue
            if i % j == 0:
                sol = int(i/j)
                break
            elif j % i == 0:
                sol = int(j/i)
                break
        diff += sol

    print(f"Result of Puzzle 2 is: {diff}.")


def measure(fn, params):
    start_fn = timer()
    fn(params)
    stop_fn = timer()
    print(f"{fn.__name__} took {stop_fn - start_fn} to complete.")


# puzzle1(data)

measure(puzzle2, data)
measure(puzzle2_smarter, data)
