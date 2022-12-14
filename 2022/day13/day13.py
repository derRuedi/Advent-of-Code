'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/13
'''

import functools
import json

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = [[json.loads(a) for a in line.split("\n")]
            for line in f.read().split("\n\n")]


def check_order(left, right):
    match left, right:
        case int(), int():
            if left < right:
                # important for ordering
                return -1
            return left > right
        case int(), list():
            return check_order([left], right)
        case list(), int():
            return check_order(left, [right])
        case list(), list():
            for i in range(min(len(left), len(right))):
                result = check_order(left[i], right[i])
                if result:
                    return result
            return check_order(len(left), len(right))


# part 1
n = []
for i, line in enumerate(data):
    left, right = line
    if check_order(left, right) == -1:
        n.append(i+1)

print(sum(n))


# part 2
with open(input, 'r') as f:
    all_items = [json.loads(line)
                 for line in f.read().splitlines() if line != ""]

all_items.append([[2]])
all_items.append([[6]])

all_items.sort(key=functools.cmp_to_key(check_order))

print((all_items.index([[2]]) + 1) * (all_items.index([[6]]) + 1))
