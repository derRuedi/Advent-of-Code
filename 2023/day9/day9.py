'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/9
'''

# input from website
sample_input = False
input = 'day9_sample.txt' if sample_input else 'day9.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()
    data = [[int(i) for i in line.split()] for line in data]


def find_next_value(sequence):
    if all([n == 0 for n in sequence]):
        return 0
    s = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return find_next_value(s) + s[-1]


print(sum([find_next_value(seq) + seq[-1] for seq in data]))

data = [line[::-1] for line in data]
print(sum([find_next_value(seq) + seq[-1] for seq in data]))
