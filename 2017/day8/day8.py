'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/8
'''

from collections import defaultdict
from icecream import ic

# input from website
sample_input = False
input = 'day8_sample.txt' if sample_input else 'day8.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

COMPARISONS = {
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    "==": lambda a, b: a == b,
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    "!=": lambda a, b: a != b
}
registers = defaultdict(int)
max_ever = 0

# preprocess data
for line in data:
    l = line.split()
    instruction, condition = l[0:3], l[4:]

    if COMPARISONS[condition[1]](registers[condition[0]], int(condition[2])):
        if instruction[1] == "inc":
            registers[instruction[0]] += int(instruction[2])
        elif instruction[1] == "dec":
            registers[instruction[0]] -= int(instruction[2])
        else:
            print("Something wrong here")

    if registers[max(registers, key=registers.get)] > max_ever:
        max_ever = registers[max(registers, key=registers.get)]

print(registers[max(registers, key=registers.get)])
print(max_ever)
