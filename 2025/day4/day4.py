'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/4
'''
from termcolor import colored

# input from website
sample_input = False
input = 'day4_sample.txt' if sample_input else 'day4.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

grid = {(x, y): char
        for y, line in enumerate(data)
        for x, char in enumerate(line)}

xmin, *_, xmax = sorted({x for x, _ in grid.keys()})
ymin, *_, ymax = sorted({y for _, y in grid.keys()})

directions = [
    (0, -1),  # up
    (1, -1),  # up    right
    (1, 0),  # right
    (1, 1),   # down  right
    (0, 1),   # down
    (-1, 1),  # down  left
    (-1, 0),  # left
    (-1, -1),  # up    left
]


def print_grid(grid, highlight_points=None):
    print()
    for y in range(xmax+1):
        for x in range(ymax+1):
            if highlight_points and (x, y) in highlight_points:
                print(colored(grid.get((x, y), ' '),
                      "red", attrs=["bold"]), end="")
            else:
                print(grid.get((x, y), ' '), end="")
        print()
    print()


def find_removable_tp(grid):
    removable_tp = []
    for y in range(xmax+1):
        for x in range(ymax+1):
            if grid[(x, y)] == ".":
                continue
            adjacent_rolls = ""
            for dir_x, dir_y in directions:
                adjacent_rolls += grid.get((x + dir_x, y + dir_y), '.')
            if adjacent_rolls.count("@") <= 3:
                removable_tp.append((x, y))
    return removable_tp


removable_tp = find_removable_tp(grid)
print_grid(grid, removable_tp)
print(len(removable_tp))

total_removable_tp = len(removable_tp)
while len(removable_tp) != 0:
    for tp in removable_tp:
        grid[(tp[0], tp[1])] = "."
    removable_tp = find_removable_tp(grid)
    total_removable_tp += len(removable_tp)

print_grid(grid)
print(total_removable_tp)
