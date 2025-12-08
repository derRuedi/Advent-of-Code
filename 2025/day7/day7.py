'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/7
'''

# input from website
from typing import Counter


sample_input = False
input = 'day7_sample.txt' if sample_input else 'day7.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

rows = len(data)
cols = len(data[0])

start_row = -1
start_col = -1

for row, line in enumerate(data):
    if "S" in line:
        start_row = row
        start_col = line.index("S")
        break

split_counter = 0
beams = Counter({start_col: 1})

for row in range(start_row+1, rows):
    next_beams = Counter()
    for col, beam_count in beams.items():
        if (data[row][col] == "^"):
            split_counter += 1
            next_beams[col-1] += beam_count
            next_beams[col+1] += beam_count
        else:
            next_beams[col] += beam_count
    beams = next_beams

print(split_counter)
print(sum(beams.values()))
