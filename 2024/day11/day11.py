'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/11
'''

import functools
# input from website
sample_input = False
input = 'day11_sample.txt' if sample_input else 'day11.txt'
with open(input, 'r') as f:
    data = list(map(int, f.read().split()))


@functools.lru_cache(maxsize=None)
def calculate_stones(stone, blinks):
    # if we don't blink any more, a stone is just a stone, no matter what it looks like, it counts 1
    if blinks == 0:
        return 1
    # if the stone is 0, convert it to 1, reduce # of blinks, continue
    if stone == 0:
        return calculate_stones(1, blinks - 1)
    # if the stone has an even number of digits, split it in two, reduce # of blinks, continue
    elif len(str(stone)) % 2 == 0:
        x = str(stone)
        result = calculate_stones(int(x[len(x)//2:]), blinks-1)
        result += calculate_stones(int(x[:len(x)//2]), blinks-1)
        return result
    # none of the other rules apply, multiply old stone's number by 2024, reduce # of blinks, continue
    else:
        return calculate_stones(stone * 2024, blinks-1)


print(f"puzzle 1: {sum(calculate_stones(stone, 25) for stone in data)}")
print(f"puzzle 2: {sum(calculate_stones(stone, 75) for stone in data)}")
