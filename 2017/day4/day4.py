'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/4
'''

# input from website
sample_input = False
input = 'day4_sample.txt' if sample_input else 'day4.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def puzzle1(data):
    valid_passphrases = 0
    for line in data:
        elements = line.split(" ")
        unique_elements = set(elements)
        if len(elements) == len(unique_elements):
            valid_passphrases += 1
    return valid_passphrases


def puzzle2(data):
    valid_passphrases = 0
    for line in data:
        elements = line.split(" ")
        elements = ["".join(sorted(e)) for e in elements]
        unique_elements = set(elements)
        if len(elements) == len(unique_elements):
            valid_passphrases += 1
    return valid_passphrases


print(puzzle1(data))

print(puzzle2(data))
