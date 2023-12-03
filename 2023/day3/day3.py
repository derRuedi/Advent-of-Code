'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/3
'''

# input from website
from collections import defaultdict
import re
sample_input = False
input = 'day3_sample.txt' if sample_input else 'day3.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

max_x = len(data[0])
max_y = len(data)
engine_parts = []
possible_gear_part = defaultdict(list)
all_numbers = []

# for line in data:
#     print(line)
# print()

for y, line in enumerate(data):
    nums = re.findall(r"\d+", line)

    all_numbers += nums
    start_index = 0
    for n in nums:
        is_enginge_part = False
        x = line.index(n, start_index)
        start_index = x+len(n)
        ys_to_check = [o for o in [y-1, y, y+1] if o >= 0 and o < max_y]
        xs_to_check = [x+o for o in range(-1, len(n)+1)
                       if x+o >= 0 and x+o < max_x]
        points_to_check = [(_x, _y) for _y in ys_to_check
                           for _x in xs_to_check]

        for p_x, p_y in points_to_check:
            if data[p_y][p_x] not in "1234567890.":
                is_enginge_part = True
            if data[p_y][p_x] == "*":
                possible_gear_part[(p_y, p_x)].append(n)
        if is_enginge_part:
            engine_parts.append(n)

print(sum(map(int, engine_parts)))

print(sum(int(v[0]) * int(v[1])
      for v in possible_gear_part.values() if len(v) == 2))
