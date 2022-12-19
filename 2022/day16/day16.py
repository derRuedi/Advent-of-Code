'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/16
'''

import functools


# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

f = {}
g = {}

for line in data:
    valve = line[6:8]
    flow, rest = line.split("; ")
    flow = flow[flow.index("=")+1:]
    rest = rest.replace('valves', 'valve')[len('tunnels lead to valve '):]
    f[valve] = int(flow)
    g[valve] = rest.split(', ')

# for k,v in g.items():
# 		print(k, v)

cur = "AA"


@functools.lru_cache(maxsize=None)
def max_flow(cur, opened, min_left):
    if min_left <= 0:
        return 0
    best = 0
    if cur not in opened:
        val = f[cur] * (min_left - 1)
        cur_opened = tuple(sorted(opened + (cur,)))
        for adj in g[cur]:
            if f[cur] != 0:
                best = max(best, val + max_flow(adj, cur_opened, min_left-2))
            best = max(best, max_flow(adj, opened, min_left - 1))
    return best


print(max_flow(cur, (), 30))
