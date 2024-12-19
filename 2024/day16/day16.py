'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/16
'''

import networkx as nx
from termcolor import colored
import heapq

# input from website
sample_input = False
input = 'day16_sample.txt' if sample_input else 'day16.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


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
                      "light_blue", attrs=["bold"]), end="")
            elif grid[y][x] == "S":
                print(colored(grid[y][x],
                      "green", attrs=["bold"]), end="")
            elif grid[y][x] == "E":
                print(colored(grid[y][x],
                      "red", attrs=["bold"]), end="")
            else:
                print(grid[y][x], end="")
        print()
    print()


def parse_data(data):
    start = None
    end = None
    free = set()
    grid = []

    for y, line in enumerate(data):
        row = []
        for x, c in enumerate(line):
            row.append(c)
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
                free.add((x, y))
            elif c == ".":
                free.add((x, y))
        grid.append(row)

    return grid, free, start, end


def dijkstra(start, free):
    directions = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1)
    }

    rotation = ">v<^"

    to_visit = []
    visited = {
        (start, ">"): 0
    }

    heapq.heappush(to_visit, (0, ">", start))

    while to_visit:
        score, direction, position = heapq.heappop(to_visit)

        if (position, direction) in visited and visited[(position, direction)] < score:
            continue

        dx, dy = directions[direction]
        # going forward
        if (position[0] + dx, position[1] + dy) in free:
            new_position = (position[0] + dx, position[1] + dy)
            if (new_position, direction) not in visited or visited[(new_position, direction)] > score + 1:
                visited[(new_position, direction)] = score + 1
                heapq.heappush(to_visit, (score+1, direction, new_position))

        # turning
        for turn in [-1, 1]:
            new_direction = rotation[(
                rotation.index(direction) + turn) % 4]
            if (position, new_direction) not in visited or visited[(position, new_direction)] > score + 1000:
                visited[(position, new_direction)] = score + 1000
                heapq.heappush(to_visit, (score+1000, new_direction, position))

    return visited


grid, free, start, end = parse_data(data)
visited = dijkstra(start, free)
print_grid(grid)
print(min(v for k, v in visited.items() if k[0] == end))


#
#
#
#
#
# new approach with the help of networkx
data = open('day16.txt').read().splitlines()
rows, cols = len(data), len(data[0])

free = set()
G = nx.Graph()

directions = ['^', '>', 'v', '<']

for row in range(rows):
    for col in range(cols):
        char = grid[row][col]
        if char == "S":
            start = row, col, ">"
        elif char == "E":
            end = row, col, "?"

        if char != "#":
            free.add((row, col))

for row in range(rows):
    for col in range(cols):
        if (row, col) in free:
            for dir in directions:
                G.add_node((row, col, dir))

            # account for direction change
            for idx, dir in enumerate(directions):
                G.add_edge((row, col, dir), (row, col,
                           directions[(idx+1) % len(directions)]), weight=1000)
            # up
            if (row-1, col) in free:
                G.add_edge((row, col, "^"), (row-1, col, "^"), weight=1)
            # down
            if (row+1, col) in free:
                G.add_edge((row, col, "v"), (row+1, col, "v"), weight=1)
            # left
            if (row, col-1) in free:
                G.add_edge((row, col, "<"), (row, col-1, "<"), weight=1)
            # right
            if (row, col+1) in free:
                G.add_edge((row, col, ">"), (row, col+1, ">"), weight=1)

for dir in directions:
    G.add_edge((end[0], end[1], dir), end, weight=0)

dist_from_start, path = nx.single_source_dijkstra(
    G, source=start, weight='weight')
dist_from_end, path = nx.single_source_dijkstra(G, source=end, weight='weight')

# Part 1
min_cost = dist_from_start[end]
print(min_cost)

# Part 2
best_spots = {(row, col) for row, col, dir in G.nodes()
              if min_cost == (dist_from_start[row, col, dir]+dist_from_end[row, col, dir])}
print(len(best_spots))
