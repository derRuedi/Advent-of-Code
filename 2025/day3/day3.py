'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/3
'''

# input from website
sample_input = False
input = 'day3_sample.txt' if sample_input else 'day3.txt'
with open(input, 'r') as f:
    data = [list(map(int, line)) for line in f.read().splitlines()]


def find_max_joltage(battery_bank, powered_batteries):
    available_batteries = len(battery_bank)
    max_joltage = 0
    current_pos = 0
    for pos in range(powered_batteries):
        remaining_needed = powered_batteries - pos
        max_digit = -1
        max_idx = -1
        for i in range(current_pos, available_batteries - remaining_needed + 1):
            if battery_bank[i] > max_digit:
                max_digit = battery_bank[i]
                max_idx = i
        max_joltage = max_joltage * 10 + max_digit
        current_pos = max_idx + 1
    return max_joltage


print(sum(find_max_joltage(line, 2) for line in data))
print(sum(find_max_joltage(line, 12) for line in data))
