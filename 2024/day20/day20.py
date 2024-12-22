'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/20
'''

import networkx as nx
from termcolor import colored
from itertools import combinations
import heapq

# input from website
sample_input = False
input = 'day20_sample.txt' if sample_input else 'day20.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def parse_data(data):
    start = None
    end = None
    free = set()
    walls = set()
    grid = []

    for y, line in enumerate(data):
        row = []
        for x, c in enumerate(line):
            row.append(c)
            if c == "S":
                start = (x, y)
                free.add((x, y))
            elif c == "E":
                end = (x, y)
                free.add((x, y))
            elif c == ".":
                free.add((x, y))
            else:
                walls.add((x, y))
        grid.append(row)

    return grid, start, end, free, walls


def dijkstra(start, free_spaces):
    to_visit = []
    visited = {
        (start): 0,
    }

    heapq.heappush(to_visit, (0, start))

    while to_visit:
        score, (cx, cy) = heapq.heappop(to_visit)

        if (cx, cy) in visited and visited[(cx, cy)] < score:
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (cx+dx, cy+dy) in free_spaces:
                np = (cx+dx, cy+dy)
                if np not in visited or visited[np] > score + 1:
                    visited[np] = score + 1
                    heapq.heappush(to_visit, (score+1, np))
    return visited


grid, start, end, free, walls = parse_data(data)

visited = dijkstra(start, free)
shortest_path = visited[end]
# print(shortest_path)

savings = 0
for point in visited:
    # all directions behind a wall
    for dx, dy in [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (0, -1), (0, 1), (0, 2), (1, -1), (1, 0), (1, 1), (2, 0)]:
        shortcut_point = (point[0]+dx, point[1]+dy)
        if shortcut_point in visited:  # if not a wall, calculate costs
            initial_cost = visited[point] - visited[shortcut_point]
            cheat_cost = abs(point[0]-shortcut_point[0]) + \
                abs(point[1]-shortcut_point[1])
            if (initial_cost - cheat_cost) >= 100:
                savings += 1
print(savings)

savings = 0
# check for every point combination.... oh boy
for point, shortcut_point in combinations(visited, 2):
    cost = abs(point[0]-shortcut_point[0]) + \
        abs(point[1]-shortcut_point[1])
    initial_cost = visited[shortcut_point] - visited[point]
    if cost <= 20 and (initial_cost - cost) >= 100:
        savings += 1
print(savings)
