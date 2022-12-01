'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/1
'''

# quick solution

# # input from website
# with open(f'input.txt', 'r') as f:
#     data = f.read().splitlines()

# elves = []
# elve = []

# for line in data:
#     if line != "":
#         elve.append(line)
#     else:
#         elves.append(elve)
#         elve = []

# elves = [sum(map(int, e)) for e in elves]

# elves.sort(reverse=True)
# print(elves[0])
# print(sum(elves[0:3]))


# ---
# more pythonic solution

# input from website
with open('input.txt', 'r') as f:
    data = f.read()

elves = [sum(map(int, e.split("\n"))) for e in data.split("\n\n")]
elves.sort(reverse=True)
print(elves[0], sum(elves[0:3]))
