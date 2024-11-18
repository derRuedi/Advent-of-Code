'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/15
'''

# input from website
from collections import OrderedDict
sample_input = False
input = 'day15_sample.txt' if sample_input else 'day15.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()[0].split(",")


def hash_algorithm(input_string):
    current_value = 0
    for c in input_string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


sum_of_results = sum([hash_algorithm(value) for value in data])
print(sum_of_results)

boxes = {k: OrderedDict() for k in range(256)}
for value in data:
    if "-" in value:
        label = value[:-1]
        lens = None
    else:
        label, lens = value.split("=")

    label_value = hash_algorithm(label)

    if lens:    # operation =
        boxes[label_value][label] = int(lens)
    else:       # operation -
        if label in boxes[label_value]:
            del boxes[label_value][label]

focusing_power = 0
for box_no, box_content in boxes.items():
    if box_content:
        for slot_no, lens in enumerate(box_content.items()):
            focusing_power += ((box_no + 1) * (slot_no + 1) * lens[1])
print(focusing_power)
