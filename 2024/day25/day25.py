'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/25
'''

# input from website
sample_input = False
input = 'day25_sample.txt' if sample_input else 'day25.txt'
with open(input, 'r') as f:
    schematics = [section.splitlines() for section in f.read().split("\n\n")]


locks = []
# locks are schematics that have the top row filled (#) and the bottom row empty (.)
keys = []
# keys have the top row empty and the bottom row filled

for schematic in schematics:
    (locks if all(c == "#" for c in schematic[0]) else keys).append(schematic)

locks = [[s.count("#")-1 for s in list(zip(*lock))] for lock in locks]
keys = [[s.count("#")-1 for s in list(zip(*key))] for key in keys]

unique_lock_key_pairs = 0
for key in keys:
    for lock in locks:
        if all(k + l < 6 for k, l in zip(key, lock)):
            unique_lock_key_pairs += 1

print(unique_lock_key_pairs)
