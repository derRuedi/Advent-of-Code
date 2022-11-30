'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

from itertools import combinations, combinations_with_replacement, permutations
import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def preprocess_data(data, include_me=False):
    happiness = {}
    guests = set()
    if include_me:
        guests.add('Ruedi')
    for l in data:
        p = l.split(" ")
        seat1 = p[0]
        seat2 = p[-1][0:-1]
        happiness_units = int(p[3]) if p[2] == "gain" else int(p[3])*-1
        happiness[f"{seat1}->{seat2}"] = happiness_units
        if include_me:
            happiness[f"{'Ruedi'}->{seat1}"] = 0
            happiness[f"{seat1}->{'Ruedi'}"] = 0
        guests.add(seat1)
        guests.add(seat2)

    seating_arrangements = permutations(guests, len(guests))

    seating_arrangement_points = []
    for sa in seating_arrangements:
        sum = 0
        for i in range(len(sa)-1):
            sum += happiness[f"{sa[i]}->{sa[i+1]}"]
            sum += happiness[f"{sa[i+1]}->{sa[i]}"]
        sum += happiness[f"{sa[0]}->{sa[-1]}"]
        sum += happiness[f"{sa[-1]}->{sa[0]}"]
        seating_arrangement_points.append(sum)

    return max(seating_arrangement_points)


def puzzle1(data):
    print(preprocess_data(data))


def puzzle2(data):
    print(preprocess_data(data, include_me=True))


puzzle1(data)
puzzle2(data)
