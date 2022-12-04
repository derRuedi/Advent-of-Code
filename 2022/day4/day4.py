'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/4
'''

import re

pattern = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

# input from website
with open(f'input.txt', 'r') as f:
    data = f.read().splitlines()

data = [list(map(int, pattern.findall(line)[0])) for line in data]

count_p1 = 0
count_p2 = 0
for line in data:
    s1, e1, s2, e2 = line
    r1 = range(s1, e1+1)
    r2 = range(s2, e2+1)
    if all(e in r2 for e in r1) or all(e in r1 for e in r2):
        count_p1 += 1
    if any(e in r2 for e in r1):
        count_p2 += 1
print(count_p1)
print(count_p2)
