'''
    Advent of Code Day 1
    https://adventofcode.com/2015/day/1
'''

# input from website in raw format
with open('day1.input.txt', 'r') as f:
    data = f.read()


print(f'Answer to puzzle 1: {data.count("(") - data.count(")")}')

level = 0
for i, p in enumerate(data):
    if p == "(":
        level += 1
    if p == ")":
        level -= 1
    if level == -1:
        print(f"Answer to puzzle 2: {i+1}")
        break
