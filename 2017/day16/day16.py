'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/16
'''

from collections import deque

# input from website
sample_input = False
input = 'day16_sample.txt' if sample_input else 'day16.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def dance(programs: str, instructions: list):
    programs = deque(programs)
    for instruction in instructions:
        match instruction[0]:
            case "s":  # switch
                programs.rotate(int(instruction[1:]))
            case "x" | "p":  # exchange or partner
                if instruction[0] == "x":  # exchange
                    x, y = [int(i) for i in instruction[1:].split("/")]
                else:  # partner
                    x, y = instruction[1:].split("/")
                    x = programs.index(x)
                    y = programs.index(y)

                tmp = programs[x]
                programs[x] = programs[y]
                programs[y] = tmp
            case _:
                print("IN HERE- NOOOO!"*100)
                pass
    return "".join(programs)


programs = "abcde" if sample_input else "".join(
    chr(c) for c in range(97, 97+15+1))
instructions = data[0].split(",")


dance_result = dance(programs, instructions)
print(f"puzzle 1: {dance_result}")


all_dance_results = [dance_result]
while True:
    dance_result = dance(dance_result, instructions)
    if dance_result in all_dance_results:
        break
    all_dance_results.append(dance_result)

dances = 1_000_000_000
print(f"puzzle 2: {all_dance_results[(dances % len(all_dance_results))-1]}")
