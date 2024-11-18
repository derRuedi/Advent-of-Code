'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/18
'''

from collections import defaultdict

# input from website
sample_input = False
input = 'day18_sample.txt' if sample_input else 'day18.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


instructions = [[int(c) if (c.isdigit() or c.startswith("-"))
                 else c for c in l.split(" ")] for l in data]


def process_input(input):
    line = -1
    while line <= len(input)-2:
        line += 1
        instruction = input[line]

        match instruction[0]:
            case "snd":
                register["snd"] = register[instruction[1]]
            case "set":
                if isinstance(instruction[2], str):
                    register[instruction[1]] = register[instruction[2]]
                else:
                    register[instruction[1]] = instruction[2]
            case "add":
                if isinstance(instruction[2], str):
                    register[instruction[1]] += register[instruction[2]]
                else:
                    register[instruction[1]] += instruction[2]
            case "mul":
                if isinstance(instruction[2], str):
                    register[instruction[1]] *= register[instruction[2]]
                else:
                    register[instruction[1]] *= instruction[2]
            case "mod":
                if isinstance(instruction[2], str):
                    register[instruction[1]] %= register[instruction[2]]
                else:
                    register[instruction[1]] %= instruction[2]
            case "rcv":
                if register[instruction[1]] != 0:
                    register["rcv_snd"] = register["snd"]
                    print(register["rcv_snd"])
                    break
            case "jgz":
                if register[instruction[1]] > 0:
                    if isinstance(instruction[2], str):
                        line += register[instruction[2]] - 1
                    else:
                        line += instruction[2] - 1

            case _:
                print(f"Something wrong here with {instruction[0]}.")


register = defaultdict(int)
process_input(instructions)
