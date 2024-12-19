'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/19
'''
from icecream import ic
import functools

# input from website
sample_input = False
input = 'day19_sample.txt' if sample_input else 'day19.txt'
with open(input, 'r') as f:
    data = [section.splitlines() for section in f.read().split("\n\n")]

towel_patterns = tuple(data[0][0].split(", "))
designs = data[1]

# print(towel_patterns)
# print()
# for design in designs:
#     print(design)


@functools.lru_cache(maxsize=None)
def possible_design(design, patterns):

    if len(design) == 0:
        return True

    for p in patterns:
        if design.startswith(p) and possible_design(design[len(p):], patterns):
            return True
    return False


@functools.lru_cache(maxsize=None)
def num_of_possible_design(design, patterns):

    if len(design) == 0:
        return 1

    num = 0
    for p in patterns:
        if design.startswith(p):
            num += num_of_possible_design(design[len(p):], patterns)
    return num


print(sum(possible_design(design, towel_patterns) for design in designs))
print(sum(num_of_possible_design(design, towel_patterns)
      for design in designs))
