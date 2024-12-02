'''
    Advent of Code 2018
    https://adventofcode.com/2018/day/2
'''

from itertools import combinations
from collections import Counter
from icecream import ic

# input from website
sample_input = False
input = 'day2_sample.txt' if sample_input else 'day2.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


twos = 0
threes = 0

for line in data:
    c = Counter(line)
    c = c.most_common()
    a = [n[1] for n in c]
    if 2 in a:
        twos += 1
    if 3 in a:
        threes += 1

print(f"Puzzle #1: {twos*threes}")


comb = combinations(data, 2)
for i, j in comb:
    diffs = 0
    for idx, c in enumerate(i):
        if c != j[idx]:
            diffs += 1
    if diffs == 1:
        answer = [c for idx, c in enumerate(i) if c == j[idx]]
        print(f"Puzzle #2: {''.join(answer)}")
        break
