'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/18
'''

import networkx as nx

# input from website
sample_input = False
input = 'day18_sample.txt' if sample_input else 'day18.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

start = (0, 0)
end = (6, 6) if sample_input else (70, 70)

x_max = end[0]
y_max = end[1]
simulate_bytes = 12 if sample_input else 1024


def parse_data(data, x_max, y_max, no_bytes):
    incoming_bytes = [list(map(int, p.split(","))) for p in data]
    incoming_bytes = incoming_bytes[:no_bytes]
    grid = []
    for y in range(y_max + 1):
        row = []
        for x in range(x_max + 1):
            row.append("." if [x, y] not in incoming_bytes else "#")
        grid.append(row)
    return grid


def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    graph = nx.Graph()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ".":
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == ".":
                        graph.add_edge((r, c), (nr, nc))

    try:
        return nx.shortest_path(graph, source=start, target=end)
    except nx.NetworkXNoPath:
        return None


# puzzle 1
grid = parse_data(data, x_max, y_max, simulate_bytes)
print(f"puzzle 1: {len(shortest_path(grid, start, end))-1}")
print()

# puzzle 2 (takes some time, could be optimized with binary search, but nah :-D)
for i in range(len(data) - simulate_bytes):
    grid = parse_data(data, x_max, y_max, simulate_bytes+i)
    sp = shortest_path(grid, start, end)
    print(f" checking {simulate_bytes+i} of at most {len(data)}.")
    if not sp:
        break
print(f"puzzle 2: {data[i+simulate_bytes-1]}")
