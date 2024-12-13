'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/13
'''
from math import gcd
import math
import functools
import re
import sys

# input from website
sample_input = False
input = 'day13_sample.txt' if sample_input else 'day13.txt'
with open(input, 'r') as f:
    data = [section.splitlines() for section in f.read().split("\n\n")]


machines = []
for line in data:
    machine = {}
    machine["a"] = tuple(map(int, re.findall(r"[0-9]+", line[0])))
    machine["b"] = tuple(map(int, re.findall(r"[0-9]+", line[1])))
    machine["prize"] = tuple(map(int, re.findall(r"[0-9]+", line[2])))
    machines.append(machine)


@functools.lru_cache(maxsize=None)
def solve(x, y, a_presses, b_presses, x_a, y_a, x_b, y_b, x_prize, y_prize, part_two=False):
    if x > x_prize or y > y_prize:
        return float("inf")
    if not part_two:
        if a_presses > 100 or b_presses > 100:
            return float("inf")
    if x == x_prize and y == y_prize:
        return a_presses * 3 + b_presses * 1

    press_A = solve(
        x + x_a, y + y_a, a_presses + 1, b_presses, x_a, y_a, x_b, y_b, x_prize, y_prize, part_two)
    press_B = solve(
        x + x_b, y + y_b, a_presses, b_presses + 1, x_a, y_a, x_b, y_b, x_prize, y_prize, part_two)

    return min(press_A, press_B)


result = [solve(0, 0, 0, 0, machine["a"][0], machine["a"][1], machine["b"][0],
                machine["b"][1], machine["prize"][0], machine["prize"][1]) for machine in machines]

print(sum(a for a in result if a != float("inf")))

# recursion does not work for part 2, back to math

result = 0
adding = 10000000000000
for machine in machines:
    # cramer's rule
    # b = (x_a * y_prize - y_a * x_prize) / (x_a * y_b - y_a * x_b)
    # a = (x_prize - x_b * b) / x_a
    b = (machine["a"][0] * (machine["prize"][1]+adding) - machine["a"][1] * (machine["prize"]
         [0]+adding)) / (machine["a"][0] * machine["b"][1] - machine["a"][1] * machine["b"][0])
    a = ((machine["prize"][0]+adding) -
         machine["b"][0] * b) / machine["a"][0]
    if a.is_integer() and b.is_integer():
        result += int(a*3 + b)
print(result)
