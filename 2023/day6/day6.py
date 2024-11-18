'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/6
'''

# input from website
from functools import reduce


sample_input = False
input = 'day6_sample.txt' if sample_input else 'day6.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()
races = list(zip(data[0].split(), data[1].split()))[1:]


def race_boat(time, distance):
    ways_to_win = 0
    for i in range(1, time):
        travelled_distance = i*time - i ** 2
        if travelled_distance > distance:
            ways_to_win += 1
    return ways_to_win


race_ways_to_win = []
for t, d in races:
    race_ways_to_win.append(race_boat(int(t), int(d)))
print(reduce(lambda a, b: a*b, race_ways_to_win))


t = int(data[0][5:].replace(" ", ""))
d = int(data[1][9:].replace(" ", ""))
print(race_boat(t, d))
