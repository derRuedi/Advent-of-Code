'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/6
'''

from functools import reduce
from operator import add, mul

# input from website
sample_input = False
input = 'day6_sample.txt' if sample_input else 'day6.txt'
with open(input, 'r') as f:
    data = [line.split() for line in f.read().splitlines()]

data = list(zip(*data))

grand_total = 0
for line in data:
    operator = add if line[-1] == "+" else mul
    grand_total += reduce(operator, map(int, line[:-1]))
print(grand_total)


with open(input, 'r') as f:
    data = f.read().splitlines()

data = list(zip(*data))
numbers = []
chunk = []
for line in data:
    if all(i == " " for i in line):
        numbers.append(chunk)
        chunk = []
        continue
    chunk.append(line)
numbers.append(chunk)

grand_total = 0
for line in numbers:
    operator = add if [i[-1] for i in line if i[-1] != " "][0] == "+" else mul
    nums = [int("".join(l[:-1])) for l in line]
    grand_total += reduce(operator, nums)
print(grand_total)
