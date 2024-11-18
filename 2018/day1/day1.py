'''
    Advent of Code 2018
    https://adventofcode.com/2018/day/1
'''

# input from website
import time


input = 'day1.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

# puzzle 1
print(sum(int(a) for a in data))

# puzzle 2
current_frequency = 0
frequencies = set()
frequencies.add(current_frequency)
while True:
    for v in data:
        v = int(v)
        current_frequency += v
        if current_frequency in frequencies:
            print(current_frequency)
            exit()
        else:
            frequencies.add(current_frequency)
