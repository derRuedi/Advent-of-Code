'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/3
'''

import string

# input from website
with open(f'input.txt', 'r') as f:
    data = f.read().splitlines()

priorities = string.ascii_lowercase + string.ascii_uppercase

sum_of_priorities = 0
for line in data:
    first, last = line[:len(line)//2], line[len(line)//2:]
    same_item = set(c for c in first if c in last)
    sum_of_priorities += priorities.index(same_item.pop()) + 1
print(sum_of_priorities)


sum_of_priorities = 0
for i in range(0, len(data), 3):
    first, second, third = data[i], data[i+1], data[i+2]
    same_item = set(c for c in first if c in second and c in third)
    sum_of_priorities += priorities.index(same_item.pop()) + 1
print(sum_of_priorities)
