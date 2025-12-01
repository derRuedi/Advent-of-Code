'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/1
'''

from operator import add, sub

# input from website
sample_input = False
input = 'day1_sample.txt' if sample_input else 'day1.txt'
with open(input, 'r') as f:
    data = [(add if line[0] == "R" else sub, int(line[1:]))
            for line in f.read().splitlines()]

zeros = 0
dial = 50
for d in data:
    direction, amount = d
    dial = direction(dial, amount)
    if dial % 100 == 0:
        zeros += 1
print(zeros)

print("="*100)

zeros = 0
dial = 50
for d in data:
    direction, amount = d
    zeros += amount // 100
    amount = amount % 100
    prev_dial = dial
    dial = direction(dial, amount)

    if dial >= 100 or dial <= 0:
        dial = dial % 100
        if dial != prev_dial and prev_dial != 0:
            zeros += 1
print(zeros)
