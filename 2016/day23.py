'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

from collections import defaultdict
import pathlib
from time import sleep

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def preprocess_data(data):
    input = []
    for l in data:
        input.append([int(c) if (c.isdigit() or c.startswith("-"))
                     else c for c in l.replace(",", "").split(" ")])
    return input


def process_input(input, register=defaultdict(int)):
    line = -1
    while line <= len(input)-2:
        line += 1
        instruction = input[line]

        match instruction[0]:
            case "inc":
                register[instruction[1]] += 1
            case "dec":
                register[instruction[1]] -= 1
            case "jnz":
                if (type(instruction[1]) == int and instruction[1] != 0) or ((instruction[1] in register) and (register[instruction[1]] != 0)):
                    if type(instruction[2]) == int:
                        line += instruction[2] - 1
                    else:
                        line += register[instruction[2]] - 1
            case "cpy":
                if type(instruction[1]) == int:
                    register[instruction[2]] = instruction[1]
                else:
                    register[instruction[2]] = register[instruction[1]]
            case "tgl":
                instruction_to_toggle = line + register[instruction[1]]
                if instruction_to_toggle < len(input):
                    match input[instruction_to_toggle][0]:
                        case "inc":
                            input[instruction_to_toggle][0] = "dec"
                        case "dec" | "tgl":
                            input[instruction_to_toggle][0] = "inc"
                        case "jnz":
                            input[instruction_to_toggle][0] = "cpy"
                        case "cpy":
                            input[instruction_to_toggle][0] = "jnz"
            case _:
                print(f"Something wrong here with {instruction[0]}.")
    print(register["a"])


input = preprocess_data(data)

# for line in input:
#     print(line)


# # part 1
register = defaultdict(int)
register["a"] = 7
process_input(input, register)

# # part 2
# takes quite some time

# register = defaultdict(int)
# register["a"] = 12
# process_input(input, register)
