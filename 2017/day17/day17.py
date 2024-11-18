'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/17
'''
from collections import deque
from icecream import ic

# input from website
sample_input = False
steps = 3 if sample_input else 382

buffer = deque([0])
current_position = 0

for i in range(2017):
    current_position = ((current_position + steps) % len(buffer)) + 1
    buffer.insert(current_position, i+1)

print(buffer[buffer.index(2017)+1])

# ------
# no need to keep track of what's in the buffer, so don't do a buffer manipulation,
# instead calculate, how many positions come after the position we are looking for

current_position = 0
after_length = 0
after_zero = 0

for i in range(50_000_000):
    current_position = ((current_position + steps) % (1 + after_length)) + 1
    if current_position == 1:
        after_zero = i + 1
        after_length += 1
    else:
        after_length += 1

print(after_zero)
