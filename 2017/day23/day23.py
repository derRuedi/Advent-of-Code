'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/23
'''
from collections import defaultdict
import time

# input from website
sample_input = False
input = 'day23_sample.txt' if sample_input else 'day23.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


instructions = [[int(c) if (c.isdigit() or c.startswith("-"))
                 else c for c in l.split(" ")] for l in data]


def process_input(input):
    line = -1
    count = 0
    while line <= len(input)-2:
        line += 1
        instruction = input[line]
        match instruction[0]:
            case "set":
                if isinstance(instruction[2], str):
                    register[instruction[1]] = register[instruction[2]]
                else:
                    register[instruction[1]] = instruction[2]
            case "sub":
                if isinstance(instruction[2], str):
                    register[instruction[1]] -= register[instruction[2]]
                else:
                    register[instruction[1]] -= instruction[2]
            case "mul":
                count += 1
                if isinstance(instruction[2], str):
                    register[instruction[1]] *= register[instruction[2]]
                else:
                    register[instruction[1]] *= instruction[2]
            case "jnz":
                if isinstance(instruction[1], str) and register[instruction[1]] != 0:
                    if isinstance(instruction[2], str):
                        line += register[instruction[2]] - 1
                    else:
                        line += instruction[2] - 1
                if isinstance(instruction[1], int) and instruction[1] != 0:
                    if isinstance(instruction[2], str):
                        line += register[instruction[2]] - 1
                    else:
                        line += instruction[2] - 1

            case _:
                print(f"Something wrong here with {instruction[0]}.")
        print(register["h"])
    print(count)


register = defaultdict(int)
process_input(instructions)

print("="*100)

register = defaultdict(int)
register["a"] = 1
process_input(instructions)
