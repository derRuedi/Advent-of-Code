'''
    Advent of Code {year}
    https://adventofcode.com/{year}/day/{day}
'''

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

for line in data:
    print(line)
