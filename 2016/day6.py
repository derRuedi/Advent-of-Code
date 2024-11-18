'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib
from collections import Counter

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()

# transform the input
# input = [[] for i in data[0]]
# for line in data:
#     for i, c in enumerate(line):
#         input[i].append(c)

# transform the input - same result as code above
input = ["".join(c) for c in zip(*data)]

for line in input:
    c = Counter(line).most_common()[0][0]
    print(c, end="")
print()


for line in input:
    c = Counter(line).most_common()[-1][0]
    print(c, end="")
print()
