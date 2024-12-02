'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/1
'''

# input from website
from collections import Counter
sample_input = False
input = 'day1_sample.txt' if sample_input else 'day1.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

# read the input data and convert it
data = [list(map(int, line.split())) for line in data]

# create the two lists
left, right = list(zip(*data))

# sort them
left = sorted(list(left))
right = sorted(list(right))

# calculate the distance
print(f"puzzle 1: {sum(abs(l-r) for l, r in zip(left, right))}")

# calculate the similarity score
c = Counter(right)
print(f"puzzle 2: {sum(l*c[l] for l in left)}")
