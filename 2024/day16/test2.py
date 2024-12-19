import networkx as nx

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
            start = row, col, "?"

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
