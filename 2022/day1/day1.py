'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/1
'''

# input from website
with open('input.txt', 'r') as f:
    data = f.read()

elves = [sum(map(int, e.splitlines())) for e in data.split("\n\n")]
elves.sort(reverse=True)

print(elves[0], sum(elves[0:3]))
