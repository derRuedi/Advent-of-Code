'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/7
'''

from itertools import product
from icecream import ic

# input from website
sample_input = False
input = 'day7_sample.txt' if sample_input else 'day7.txt'
with open(input, 'r') as f:
    data = [[int(l), list(map(int, r.split()))] for l, r in [d.split(": ")
                                                             for d in f.read().splitlines()]]


def test_equation(equation, operators=['+', '*']):
    test_value, numbers = equation
    length = len(numbers) - 1

    combinations = [list(p) for p in product(operators, repeat=length)]

    for positions in combinations:

        n = numbers[:]
        operators = positions[:]

        a = n.pop(0)
        b = n.pop(0)
        operator = operators.pop(0)

        while_continue = True

        while while_continue:
            if operator == "+":
                a += b
            elif operator == "*":
                a *= b
            elif operator == "|":
                a = int(str(a) + str(b))
            else:
                exit(-1)
            if a > test_value:
                while_continue = False
                continue
            if not (operators) or not (combinations):
                if a == test_value:
                    return True
                else:
                    while_continue = False
                    continue
            else:
                b = n.pop(0)
                operator = operators.pop(0)


total_calibration_result = 0
for idx, line in enumerate(data):
    # print(idx)
    if test_equation(line):
        total_calibration_result += line[0]
print(total_calibration_result)


total_calibration_result = 0
for idx, line in enumerate(data):
    print(idx)
    if test_equation(line, ['+', '*', '|']):
        total_calibration_result += line[0]
print(total_calibration_result)
