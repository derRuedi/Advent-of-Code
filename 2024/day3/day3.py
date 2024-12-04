'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/3
'''

import re
import math

# input from website
sample_input = False
input = 'day3_sample.txt' if sample_input else 'day3.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
overall_result = 0
for line in data:
    multipliers = re.findall(regex, line)
    overall_result += sum(int(i)*int(j) for i, j in multipliers)
print(f"puzzle 1: {overall_result}")

regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
overall_result = 0
do = True
for line in data:
    matches = re.findall(regex, line)
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        else:
            if not do:
                continue
            overall_result += math.prod(map(int,
                                            re.findall(r"[0-9]{1,3}", match)))
print(f"puzzle 2: {overall_result}")
