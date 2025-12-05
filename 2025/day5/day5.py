'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/5
'''

# input from website
sample_input = False
input = 'day5_sample.txt' if sample_input else 'day5.txt'
with open(input, 'r') as f:
    ranges, ingredients = f.read().split('\n\n')


ranges = [list(map(int, line.split('-'))) for line in ranges.splitlines()]
ingredients = [int(ingrdient) for ingrdient in ingredients.splitlines()]


def is_fresh_ingredient(ingredient_id, ranges):
    for r in ranges:
        if r[0] <= ingredient_id <= r[1]:
            return True
    return False


print(sum(is_fresh_ingredient(i_id, ranges) for i_id in ingredients))

# I figured brute force won't work, still had to try - haha :-)

# fresh_ids = set()
# for idx, r in enumerate(ranges):
#     print(idx, len(ranges))
#     for i in range(r[0], r[1]+1):
#         fresh_ids.add(i)

# print(len(fresh_ids))

# merge intervals instead
# sort by range start
ranges.sort(key=lambda x: x[0])
consolidates_ranges = [ranges[0]]
for r in ranges[1:]:
    # if new range start is smaller than current range end
    if consolidates_ranges[-1][1] >= r[0]:
        # set current range end to the bigger value of the two ranges
        consolidates_ranges[-1][1] = max(r[1], consolidates_ranges[-1][1])
    else:
        # otherwise it is a new range entirely and since we sorted, nothing else to do
        consolidates_ranges.append(r)

# count inclusive ids
print(sum(e-s+1 for s, e in consolidates_ranges))
