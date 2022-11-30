'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

from collections import defaultdict
import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def preprocess_data(data):
    input = []
    for l in data:
        input.append(l.replace(",", "").split(" "))
    return input


def process_input(input, a, b):
    register = defaultdict(int)
    register["a"] = a
    register["b"] = b
    line = -1
    while line <= len(input)-2:
        line += 1
        instruction = input[line]
        match instruction[0]:
            case "hlf":
                register[instruction[1]] //= 2

            case "tpl":
                register[instruction[1]] *= 3

            case "inc":
                register[instruction[1]] += 1

            case "jmp":
                line += int(instruction[1]) - 1
            case "jie":
                if register[instruction[1]] % 2 == 0:
                    line += int(instruction[2]) - 1
            case "jio":
                if register[instruction[1]] == 1:
                    line += int(instruction[2]) - 1

    print(register["b"])


input = preprocess_data(data)

# part 1
process_input(input, 0, 0)

# part 2
process_input(input, 1, 0)
