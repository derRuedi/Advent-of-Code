'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/8
'''

# input from website
from math import sqrt
from itertools import combinations
from functools import reduce
import networkx as nx

sample_input = False
input = 'day8_sample.txt' if sample_input else 'day8.txt'
with open(input, 'r') as f:
    points = [list(map(int, line.split(",")))
              for line in f.read().splitlines()]


def distance(p, q):
    return sqrt((p[0] - q[0])*(p[0] - q[0]) + (p[1] - q[1])*(p[1] - q[1]) + (p[2] - q[2])*(p[2] - q[2]))


distances = [[p[0], p[1], distance(p[0], p[1])]
             for p in combinations(points, 2)]
distances.sort(key=lambda x: x[2])

G = nx.Graph()

for i in range(len(distances)):
    p, q, _ = distances[i]
    G.add_edge(tuple(p), tuple(q))
    # part 1
    if i == (10 - 1 if sample_input else 1000 - 1):
        g = list(nx.connected_components(G))
        g.sort(key=lambda x: len(x), reverse=True)
        print(reduce(lambda x, y: x*y, [len(i) for i in g[:3]]))
    # part 2
    if len(list(nx.connected_components(G))) == 1 and len(list(nx.connected_components(G))[0]) == len(points):
        print(p[0] * q[0])
        break
