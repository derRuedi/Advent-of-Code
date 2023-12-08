'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/8
'''
import re
from math import lcm

# input from website
sample_input = False
input = 'day8_sample.txt' if sample_input else 'day8.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

instructions = data[0]
network = {source: {"L": left, "R": right}
           for line in data[2:]
           for source, left, right in [re.findall(r"(\w+)", line)]}


def calculate_steps(start, end):
    steps = 0
    current = start
    while current not in end:
        direction = instructions[steps % len(instructions)]
        next = network[current][direction]
        current = next
        steps += 1
    return steps


start = "AAA"
end = ["ZZZ"]
print(calculate_steps(start, end))


starting_nodes = [n for n in network if n.endswith("A")]
ending_nodes = [n for n in network if n.endswith("Z")]
steps = []
for start in starting_nodes:
    steps.append(calculate_steps(start, ending_nodes))
print(lcm(*steps))
