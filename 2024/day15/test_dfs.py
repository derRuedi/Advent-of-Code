from termcolor import colored
from collections import deque

DIRECTIONS = {
    "^": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1)
}


def print_grid(grid):
    print()
    y_min = 0
    x_min = 0
    y_max = len(grid)
    x_max = len(grid[0])
    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            if grid[y][x] == "#":
                print(colored(grid[y][x],
                      "red", attrs=["bold"]), end="")
            elif grid[y][x] == "O":
                print(colored(grid[y][x],
                      "blue", attrs=["bold"]), end="")
            elif grid[y][x] == "@":
                print(colored(grid[y][x],
                      "yellow", attrs=["bold"]), end="")
            else:
                print(grid[y][x], end="")
        print()
    print()


def get_train(grid, move, pos):
    q = deque([pos])
    seen = set()
    train = []
    dx, dy = DIRECTIONS[move]

    while q:
        x, y = q.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        if grid[y][x] == ".":
            continue
        elif grid[y][x] == "#":
            return False, []
        train.append((x, y))
        assert grid[y][x] in {"[", "]", "@"}
        if grid[y][x] == "[":
            if (x + 1, y) not in seen and move != ">":
                q.append((x + 1, y))
        elif grid[y][x] == "]":
            if (x - 1, y) not in seen and move != "<":
                q.append((x - 1, y))
        q.append((x+dx, y+dy))
    return True, train


data = """##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############
"""


grid = []
for y, line in enumerate(data.splitlines()):
    row = []
    for c in line:
        row.append(c)
        if c == "@":
            pos = (line.index("@"), y)
    grid.append(row)

print_grid(grid)

print(get_train(grid, "^", pos))
