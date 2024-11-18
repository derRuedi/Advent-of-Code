'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/5
'''
from itertools import chain

# input from website
sample_input = False
input = 'day5_sample.txt' if sample_input else 'day5.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

seeds = [int(i) for i in data[0][7:].split()]
all_mappings = []
mapping = {}

for line in data[2:]:
    if line and line[0].isalpha():
        map_name = line.split()[0]
        mapping["name"] = map_name
        all_mappings.append(mapping)
    elif line == "":
        mapping = {}
    else:
        mapping.setdefault("data", []).append([int(i) for i in line.split()])
        mapping.setdefault("ranges", []).append([range(int(s), int(s)+int(line.split()[-1]))
                                                 for s in line.split()[:2]])


def print_mappings(mappings):
    for mapping in mappings:
        for k, v in mapping.items():
            print(f"{k}:\t{v}")
        print()


def find_mapping(seed, mapping):
    for r in mapping["ranges"]:
        if seed in r[1]:
            return r[0][0]+r[1].index(seed)
    return seed


def find_minimum_location(seeds, mappings):
    locations = []
    for seed in seeds:
        location = seed
        for mapping in mappings:
            location = find_mapping(location, mapping)
        locations.append(location)
    return min(locations)


print(find_minimum_location(seeds, all_mappings))

seeds = chain(range(seeds[0], seeds[0] + seeds[1]),
              range(seeds[2], seeds[2] + seeds[3]))

print(find_minimum_location(seeds, all_mappings))
