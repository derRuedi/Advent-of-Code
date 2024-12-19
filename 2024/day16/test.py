import networkx as nx

grid = open('day16.txt').read().splitlines()
NR, NC = len(grid), len(grid[0])

board = set()
G = nx.Graph()

dirs = ['^', '>', 'v', '<']

for r in range(NR):
    for c in range(NC):
        ch = grid[r][c]

        if ch == 'S':
            start = r, c, '>'
        elif ch == 'E':
            end = r, c, '?'

        if ch != '#':
            board.add((r, c))

for r in range(NR):
    for c in range(NC):
        if (r, c) in board:

            for dir in dirs:
                G.add_node((r, c, dir))

            for i, dir in enumerate(dirs):
                G.add_edge((r, c, dir), (r, c, dirs[(i+1) % 4]), weight=1000)

            if (r-1, c) in board:
                G.add_edge((r, c, '^'), (r-1, c, '^'), weight=1)

            if (r+1, c) in board:
                G.add_edge((r, c, 'v'), (r+1, c, 'v'), weight=1)

            if (r, c-1) in board:
                G.add_edge((r, c, '<'), (r, c-1, '<'), weight=1)

            if (r, c+1) in board:
                G.add_edge((r, c, '>'), (r, c+1, '>'), weight=1)

for dir in dirs:
    G.add_edge((end[0], end[1], dir), end, weight=0)

dist_from_start, _ = nx.single_source_dijkstra(
    G, source=start, weight='weight')
dist_from_end, _ = nx.single_source_dijkstra(G, source=end, weight='weight')

# Part 1
min_cost = dist_from_start[end]
print(min_cost)

# Part 2
spots = {(r, c) for r, c, d in G.nodes()
         if min_cost == (dist_from_start[r, c, d]+dist_from_end[r, c, d])}
print(len(spots))
