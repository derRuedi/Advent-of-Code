'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/15
'''
from termcolor import colored
from collections import deque

# input from website
sample_input = False
input = 'day15_sample.txt' if sample_input else 'day15.txt'
with open(input, 'r') as f:
    data = [section.splitlines() for section in f.read().split("\n\n")]

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


def puzzle1():
    pos = None
    grid = []
    for y, line in enumerate(data[0]):
        row = []
        for c in line:
            row.append(c)
            if c == "@":
                pos = (line.index("@"), y)
        grid.append(row)

    moves = "".join(data[1])

    print_grid(grid)

    for move in moves:
        train = []
        dx, dy = DIRECTIONS[move]

        rx, ry = pos
        can_move = False
        movables = 0

        while True:
            if grid[ry][rx] in ["@", "O"]:  # things to move
                train.append((rx, ry))
                movables += 1
            elif grid[ry][rx] == "#":  # hitting a wall / can't move
                break
            else:
                if grid[ry][rx] == ".":  # can move
                    can_move = True
                    break
            rx += dx  # check next
            ry += dy  # check next

        if not can_move:  # if we can't move due to a wall
            continue  # go to the next movement

        # now move the whole train (and the robot, obviously)
        for tx, ty in train[::-1]:
            if grid[ty][tx] == "@":
                pos = (pos[0] + dx, pos[1]+dy)
            grid[ty+dy][tx+dx] = grid[ty][tx]
            grid[ty][tx] = "."

    total = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "O":
                total += ((y * 100) + x)

    print_grid(grid)
    print(total)


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


def puzzle2():
    pos = None
    grid = []
    for y, line in enumerate(data[0]):
        row = []
        for c in line:
            if c == ".":
                row.append(".")
                row.append(".")
            elif c == "#":
                row.append("#")
                row.append("#")
            elif c == "O":
                row.append("[")
                row.append("]")
            elif c == "@":
                pos = (line.index("@")*2, y)
                row.append("@")
                row.append(".")
        grid.append(row)

    moves = "".join(data[1])
    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "<": (-1, 0),
        "v": (0, 1)
    }

    print_grid(grid)

    for move in moves:
        dx, dy = directions[move]
        can_move, train = get_train(grid, move, pos)
        if not can_move:  # if we can't move
            continue  # go to the next movement

        # now move the whole train (and the robot, obviously)
        for tx, ty in train[::-1]:
            if grid[ty][tx] == "@":
                pos = (pos[0] + dx, pos[1]+dy)
            grid[ty+dy][tx+dx] = grid[ty][tx]
            grid[ty][tx] = "."

    total = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "[":
                total += ((y * 100) + x)

    print_grid(grid)
    print(total)


puzzle1()
puzzle2()
