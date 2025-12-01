'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/23
'''

import networkx as nx

# input from website
sample_input = False
input = 'day23_sample.txt' if sample_input else 'day23.txt'
with open(input, 'r') as f:
    data = [c.split("-") for c in f.read().splitlines()]


def create_lan(edges):
    lan = {}
    for u, v in edges:
        lan.setdefault(u, set()).add(v)
        lan.setdefault(v, set()).add(u)
    return lan


def find_triangles(lan):
    triangles = set()
    for u in lan:
        for v in lan[u]:
            common_neighbors = lan[u] & lan[v]
            for w in common_neighbors:
                triangle = tuple(sorted([u, v, w]))
                triangles.add(triangle)
    return triangles


lan = create_lan(data)
triangles = find_triangles(lan)
print(sum(1 for t in triangles if any(map(lambda x: x.startswith("t"), t))))


G = nx.Graph()

for n1 in lan:
    for n2 in lan[n1]:
        G.add_edge(n1, n2)

all_cliques = nx.find_cliques(G)
largest_clique = max(all_cliques, key=len)

print(",".join(sorted(largest_clique)))
