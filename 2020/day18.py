'''
    Advent of Code Day 18
    https://adventofcode.com/2020/day/18
'''

# input from website in raw format
data = []
with open('day18.input.txt', 'r') as f:
    data = f.read().splitlines()

sample_data = [
	"1 + 2 * 3 + 4 * 5 + 6",                            # 71        # 231
    "1 + (2 * 3) + (4 * (5 + 6))",                      # 51        # 51
    "2 * 3 + (4 * 5)",                                  # 26        # 46
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",                      # 437       # 1445
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",        # 12240     # 669060
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",  # 13632     # 23340
]

import re

def calc_result(expr):
    # check if there are parenthesis
    # if there are no parentheses
    if expr.find("(") == -1:
        # we should have a basic formula that we can calulate
        [num1, op, num2, rest] = re.match("^([0-9-]+)([+*])([0-9-]+)([^0-9].*)?$", expr).groups()
        if op == "+":
            result = int(num1) + int(num2)
        else:
            result = int(num1) * int(num2)

        if rest==None:
            # if there is nothing else to calculate, return result
            return result
        else:
            # rest already contains an operator; the "+" here is just for string concatenation
            return calc_result(str(result) + rest)

    # if there are parentheses
    else:
        # find the first innermost group
        [before, middle, after] = re.match("^(.*?)\(([^()]+)\)(.*)$", expr).groups()
        # if the parenthesis surround the entire expression
        if before == "" and after == "":
            calc_result(middle)
        else:
            return calc_result(before + str(calc_result(middle)) + after)


def calc_result_adv(expr):
    # if it is a number, return it as such
    if expr.isnumeric():
        return int(expr)
    # check for simple addition of two numbers
    elif re.match("^([0-9]+)\+([0-9]+)$", expr):
        [num1, num2] = re.match("^([0-9]+)\+([0-9]+)$", expr).groups()
        return int(num1) + int(num2)
    # check for simple multiplication of two numbers
    elif re.match("^([0-9]+)\*([0-9]+)$", expr):
        [num1, num2] = re.match("^([0-9]+)\*([0-9]+)$", expr).groups()
        return int(num1) * int(num2)
    # find inner most parentheses
    elif re.match("^(.*)\(([^)]*)\)(.*)$", expr):
        [before, middle, after] = re.match("^(.*)\(([^)]*)\)(.*)$", expr).groups()
        return calc_result_adv(before + str(calc_result_adv(middle)) + after)
    # don't match from the front, but from the back, i.e. first multiplication, then addition
    # find blocks linked by multiplication
    elif re.match("^(.*?)\*(.*)$", expr):
        # don't match from the front / first multiplication, but from the last
        [left, right] = re.match("^(.*)\*(.*)$", expr).groups()
        return calc_result_adv(left) * calc_result_adv(right)
    # find blocks linked by addition
    elif re.match("^(.*?)\+(.*)$", expr):
        # don't match from the front / first addition, but from the last
        [left, right] = re.match("^(.*)\+(.*)$", expr).groups()
        return calc_result_adv(left) + calc_result_adv(right)
    else:
        print("ooooops")



def do_homework(data, fn):
    sum = 0
    for line in data:
        line = line.replace(" ", "")
        sum += fn(line)
    return sum

print(do_homework(data, calc_result))
print(do_homework(data, calc_result_adv))

# for line in sample_data:
#     line = line.replace(" ", "")
#     print(calc_result_adv(line))