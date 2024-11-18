'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/3
'''

from icecream import ic
from math import sqrt


# input from website
sample_input = False
input = 'day3_sample.txt' if sample_input else 'day3.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

input = int(data[0])


def puzzle1(input):
    spiral_loops = 0
    side_length = 1
    numbers = 1
    while input > numbers:
        side_length += 2
        numbers += (side_length*4 - 4)
        spiral_loops += 1

    length = int(sqrt(numbers))

    # create all corner values, plus the lower right one twice (lower and upper value) to be able to create ranges
    corners = [numbers - (length - 1)*i for i in range(5)]
    corners.sort()

    ranges = list(map(range, [i+1 for i in corners], corners[1:]))

    # remove the lower value corner, since it was only used to create the appropriate ranges
    corners.pop(0)

    if input in corners:
        steps = spiral_loops
    else:
        for r in ranges:
            if input in r:
                middle = (r[0] + r[-1]) // 2
                steps = spiral_loops + abs(middle - input)
                break

    return steps


def puzzle2(input):
    # greetings from The On-Line Encyclopedia of Integer Sequences
    # https://oeis.org/A141481
    square_spiral_of_sums = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806, 880, 931, 957, 1968, 2105, 2275, 2391, 2450, 5022, 5336, 5733, 6155, 6444, 6591, 13486, 14267, 15252,
                             16295, 17008, 17370, 35487, 37402, 39835, 42452, 45220, 47108, 48065, 98098, 103128, 109476, 116247, 123363, 128204, 130654, 266330, 279138, 295229, 312453, 330785, 349975, 363010, 369601, 752688, 787032, 830037, 875851, 924406]
    i = 0
    while i < len(square_spiral_of_sums) and input > square_spiral_of_sums[i]:
        i += 1
    return square_spiral_of_sums[i]


print(f"Answer to puzzle #1 is: {puzzle1(input)}")
print(f"Answer to puzzle #2 is: {puzzle2(input)}")
