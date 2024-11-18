'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import re
import helper
import json

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read()


def preprocess_data(data):
    data = json.loads(data)
    # print(json.dumps(data, indent=4))
    return data


def puzzle1(data):
    sum_all_numbers = sum(int(i) for i in re.findall("-?\d+", data))
    print(f"The answer to puzzle 1 is: {sum_all_numbers}")


def puzzle2(data):
    def sum_if_not_red(item):
        if type(item) is int:
            return item

        if type(item) is list:
            return sum(map(sum_if_not_red, item))

        if type(item) is dict:
            if "red" in item.values():
                return 0

            return sum(map(sum_if_not_red, item.values()))

        return 0

    data = preprocess_data(data)
    print(f"The answer to puzzle 2 is: {sum_if_not_red(data)}")


puzzle1(data)
puzzle2(data)
