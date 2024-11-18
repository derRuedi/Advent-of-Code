'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/6
'''

# input from website
with open(f'input.txt', 'r') as f:
    data = f.read()


def find_marker(marker_length):
    for i in range(0, len(data) - marker_length):
        if len(set(data[i:i+marker_length])) == marker_length:
            print(i+marker_length)
            break


for x in (4, 14):
    find_marker(x)
