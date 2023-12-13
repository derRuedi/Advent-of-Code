'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/13
'''
import numpy as np
from icecream import ic

# input from website
sample_input = False
input = 'day13_sample.txt' if sample_input else 'day13.txt'
with open(input, 'r') as f:
    patterns = [{"data": np.array([list(s) for s in line.split()]), "first": set(), "second": set()}
                for line in f.read().split("\n\n")]


def get_horizontal(arr, i):
    return arr[i, :]


def get_vertical(arr, i):
    return arr[:, i]


def toggle(s):
    return "#" if s == "." else "."


def check_mirroring(arr, orientation="horizontal", ignore=None):
    if orientation == "horizontal":
        arr_func = get_horizontal
        length = arr.shape[0]
    else:
        arr_func = get_vertical
        length = arr.shape[1]

    for i in range(length - 1):
        j = i + 1
        valid = False
        if all(arr_func(arr, i) == arr_func(arr, j)) and j != ignore:
            i2, j2 = i-1, j+1
            valid = True
            while i2 >= 0 and j2 < length:
                if all(arr_func(arr, i2) == arr_func(arr, j2)):
                    i2 = i2 - 1
                    j2 = j2 + 1
                    valid = True
                else:
                    valid = False
                    break
        if valid:
            return j
    return 0


summed_up_1 = 0
summed_up_2 = 0
for pattern in patterns:
    # part 1
    arr = pattern["data"]
    for orientation in ["horizontal", "vertical"]:
        position = 0
        position = check_mirroring(arr, orientation)
        if position:
            pattern["first"].add((orientation, position))
        summed_up_1 += position * 100 if orientation == "horizontal" else position

    # part 2
    size = arr.size
    shape = arr.shape
    for i in range(size):
        row, column = i // shape[1], i % shape[1]
        arr[row][column] = toggle(arr[row][column])
        for orientation in ["horizontal", "vertical"]:
            position = 0
            ignore = None
            tmp = list(pattern["first"])[0]
            if tmp[0] == orientation:
                ignore = tmp[1]
            position = check_mirroring(arr, orientation, ignore)
            if position:
                pattern["second"].add((orientation, position))
        arr[row][column] = toggle(arr[row][column])

    new_reflection = pattern["second"] - pattern["first"]
    tmp = list(new_reflection)
    summed_up_2 += tmp[0][1] * \
        100 if tmp[0][0] == "horizontal" else tmp[0][1]

print(summed_up_1)
print(summed_up_2)
