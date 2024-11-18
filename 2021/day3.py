'''
    Advent of Code Day 3
    https://adventofcode.com/2021/day/3
'''

data = []
with open("day3.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]


def puzzle1(data):
    length_binary_number = len(data[0])
    amount_binary_numbers = len(data)

    gamma_rate = ""

    for i in range(length_binary_number):
        bit = ""
        for line in data:
            bit += line[i]

        sum = 0
        for i in bit:
            sum += int(i)

        if sum > amount_binary_numbers // 2:
            gamma_rate += "1"
        else:
            gamma_rate += "0"

    epsilon_rate = "".join(["0" if i == "1" else "1" for i in gamma_rate])
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_item_of_common_bits(data, position=0, mostCommon=True):
    bit = ""
    for line in data:
        bit += line[position]

    if mostCommon:
        common_bit = "0" if (bit.count("0") > bit.count("1")) else "1"
    else:
        common_bit = "0" if (bit.count("0") <= bit.count("1")) else "1"

    data = [i for i in data if i[position] == common_bit]

    if len(data) == 1:
        return data[0]

    return get_item_of_common_bits(data, position + 1, mostCommon)


def puzzle2(data):
    oxygen_generator_rating = get_item_of_common_bits(data)
    CO2_scrubber_rating = get_item_of_common_bits(data, mostCommon=False)
    return int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
