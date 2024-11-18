'''
    Advent of Code Day 7
    https://adventofcode.com/2021/day/7
'''

data = []
with open("day7.input.txt", "r") as f:
    data = [int(i) for i in f.read().splitlines()[0].split(",")]

sample_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def calculate_median(data):
    sorted_data = sorted(data)
    middle_element = len(data) // 2
    if len(data) % 2 == 0:
        return (sorted_data[middle_element] +
                sorted_data[middle_element-1]) // 2
    else:
        return sorted_data[middle_element]


def calculate_constant_fuel(data, position):
    fuel = 0
    for num in data:
        fuel += abs(num - position)
    return fuel


def calculate_linear_fuel(data, position):
    fuel = 0
    for num in data:
        fuel += sum(range(1, abs(num - position) + 1))
    return fuel


def puzzle1(data):
    return calculate_constant_fuel(data, calculate_median(data))


def puzzle2(data):
    fuel_necessary_for_position = []
    for position in range(0, len(data)):
        fuel_necessary_for_position.append(
            calculate_linear_fuel(data, position))

    minimum_necessary_fuel = min(fuel_necessary_for_position)

    # minimum_necessary_fuel_position = fuel_necessary_for_position.index(
    #     minimum_necessary_fuel)

    return minimum_necessary_fuel


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
