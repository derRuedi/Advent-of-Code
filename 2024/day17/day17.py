'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/17
'''

import re
from operator import xor

# input from website
sample_input = False
input = 'day17_sample.txt' if sample_input else 'day17.txt'
with open(input, 'r') as f:
    data = [section.splitlines() for section in f.read().split("\n\n")]


def parse_data(data):
    rs = re.findall(r"\d+", "".join(data[0]))
    r = {
        "a": int(rs[0]),
        "b": int(rs[1]),
        "c": int(rs[2])
    }

    p = list(map(int, data[1][0].split(": ")[1].split(",")))
    return r, p


def run_program(r, p):
    output = []
    pointer = 0
    while not len(p[pointer:]) < 2:
        opcode = p[pointer]
        operand = p[pointer+1]
        pointer += 2
        combo_operand = None
        match operand:
            case 0 | 1 | 2 | 3:
                combo_operand = operand
            case 4:
                combo_operand = r["a"]
            case 5:
                combo_operand = r["b"]
            case 6:
                combo_operand = r["c"]
            case _:
                print(f"Something wrong here with operand '{operand}'.")

        match opcode:
            case 0:  # adv
                r["a"] = r["a"] // (1 << combo_operand)
            case 1:  # bxl
                r["b"] = xor(r["b"], operand)
            case 2:  # bst
                r["b"] = combo_operand % 8
            case 3:  # jnz
                if r["a"] != 0:
                    pointer = operand
            case 4:  # bxc
                r["b"] = xor(r["b"], r["c"])
            case 5:  # out
                output.append(combo_operand % 8)
            case 6:  # bdv
                r["b"] = r["a"] // (1 << combo_operand)
            case 7:  # cdv
                r["c"] = r["a"] // (1 << combo_operand)
            case _:
                print(f"Something wrong here with operand '{operand}'.")
                print(f"pointer - {pointer}, operand - {operand}, combo_operand - {
                    combo_operand}, opcode - {opcode}, output - {output}")
    return output


def solve_1():
    register, program = parse_data(data)
    output = run_program(register, program)
    print("puzzle 1:", ",".join(map(str, output)))


def solve_2():
    register, program = parse_data(data)
    valid = [0]
    for length in range(1, len(program) + 1):
        old = valid
        valid = []
        for num in old:
            for offset in range(8):
                new = 8 * num + offset
                if run_program({"a": new, "b": 0, "c": 0}, program) == program[-length:]:
                    valid.append(new)
    print(min(valid))


solve_1()
solve_2()
