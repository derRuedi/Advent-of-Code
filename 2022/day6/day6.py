'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/6
'''

from itertools import permutations

# input from website
with open(f'input.txt', 'r') as f:
    data = f.read()


def find_marker(marker_length=4):
    for i in range(0, len(data) - marker_length):
        if all(a[0] != a[1] for a in permutations(data[i:i+marker_length], 2)):
            print(i+marker_length)
            break


find_marker()
find_marker(14)
