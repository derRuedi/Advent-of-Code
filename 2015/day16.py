'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper
import re

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()

ticket_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def preprocess_data(data):
    aunt_sues = []
    for i, line in enumerate(data):
        # Sue 482: children: 5, perfumes: 5, cats: 1
        sue_properties = re.sub(
            r"^Sue \d+: ", "", line).replace(" ", "").split(",")
        aunt_sue = {k.split(":")[0]: int(k.split(":")[1])
                    for k in sue_properties}
        aunt_sue["matches"] = 0
        aunt_sue["Sue"] = i+1
        aunt_sues.append(aunt_sue)
    return aunt_sues


def puzzle1(data):
    aunt_sues = preprocess_data(data)
    for aunt_sue in aunt_sues:
        for k, v in ticket_tape.items():
            if k in aunt_sue and v == aunt_sue[k]:
                aunt_sue["matches"] += 1

    for aunt_sue in aunt_sues:
        if aunt_sue["matches"] == 3:
            print(aunt_sue)


def puzzle2(data):
    aunt_sues = preprocess_data(data)
    for aunt_sue in aunt_sues:
        for k, v in ticket_tape.items():
            if k in aunt_sue:
                if (k == "cats" or k == "trees") and v < aunt_sue[k]:
                    aunt_sue["matches"] += 1
                elif (k == "pomeranians" or k == "goldfish") and v > aunt_sue[k]:
                    aunt_sue["matches"] += 1
                elif v == aunt_sue[k]:
                    aunt_sue["matches"] += 1

    for aunt_sue in aunt_sues:
        if aunt_sue["matches"] == 3:
            print(aunt_sue)


puzzle1(data)
print()
puzzle2(data)
