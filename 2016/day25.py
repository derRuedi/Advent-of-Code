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
    output = ""
    line = -1
    while line <= len(input)-2 and len(output) < 20:
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
            case "out":
                if type(instruction[1]) == int:
                    output += str(instruction[1])
                else:
                    output += str(register[instruction[1]])
            case _:
                print(f"Something wrong here with {instruction[0]}.")
    return output


input = preprocess_data(data)

# # part 1
output = "1"
a = 1
while not output.startswith("01"*5):
    register = defaultdict(int)
    register["a"] = a
    output = process_input(input, register)
    a += 1

# print(output)
# print(output.count("1"))
# print(len(output))
print(a-1)
