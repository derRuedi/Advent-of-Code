'''
    Advent of Code Day 2
    https://adventofcode.com/2021/day/2
'''

# input from website in raw format
data = []
with open('day2.input.txt', 'r') as f:
    data = [i.split() for i in f.read().splitlines()]

sample_data = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2)
]


def puzzle1(data):
    horizontal_pos = 0
    depth = 0
    for move, num in data:
        num = int(num)
        if move == "forward":
            horizontal_pos += num
        elif move == "down":
            depth += num
        elif move == "up":
            depth -= num
        else:
            print("Command not found.")
    # print(f"Horizontal Position: {horizontal_pos}; depth: {depth}.")
    return horizontal_pos * depth


def puzzle2(data):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for move, num in data:
        num = int(num)
        if move == "forward":
            horizontal_pos += num
            depth = depth + (num * aim)
        elif move == "down":
            aim += num
        elif move == "up":
            aim -= num
        else:
            print("Command not found.")
    # print(f"Horizontal Position: {horizontal_pos}; depth: {depth}.")
    return horizontal_pos * depth


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
