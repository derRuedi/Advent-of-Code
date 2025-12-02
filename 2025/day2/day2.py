'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/2
'''

from icecream import ic

# input from website
sample_input = False
input = 'day2_sample.txt' if sample_input else 'day2.txt'
with open(input, 'r') as f:
    id_ranges = [[int(a) for a in d.split("-")]
                 for d in f.read().split(",")]


def is_invalid_id(id):
    id = str(id)
    l = len(id)
    if l % 2 != 0:
        return False
    if id[:l//2] == id[l//2:]:
        return True
    return False


invalid_ids = []
for id_range in id_ranges:
    start, end = id_range
    for i in range(start, end+1):
        if is_invalid_id(i):
            invalid_ids.append(i)

print(sum(invalid_ids))


print("="*100)


def is_invalid_part2(id):
    id = str(id)
    l = len(id)
    r = list(range(1, l))
    for m in r:
        parts = [id[i:i+m] for i in range(0, l, m)]
        if len(set(parts)) == 1:
            return True
    return False


invalid_ids = []
for id_range in id_ranges:
    start, end = id_range
    for i in range(start, end+1):
        if is_invalid_part2(i):
            invalid_ids.append(i)

print(sum(invalid_ids))
