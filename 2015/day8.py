'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"

with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    # make sure to include an empty line at the end of your input file
    # (otherwise the -1 for the line break character kicks in and your overall solution is 1 too low)

    # length of the raw input
    # -1 for the line break character
    # minus length of the evaluated input
    print(
        f"Answer to puzzle 1: {sum(len(_) - 1 - len(eval(_)) for _ in f)}")


with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:

    # just to figure out how to count
    # for _ in f:
    #     print(f"_: {_[:-1]}")  # omit the line break
    #     print(f"len(_): {len(_) - 1}")  # omit the line break
    #     print(f"eval(_): {eval(_)}")
    #     print(f"len(eval(_)): {len(eval(_))}")

    #     print("_.count('\\'): ", end="")
    #     print(_.count('\\'))

    #     print("_.count('\"'): ", end="")
    #     print(_.count('"'))
    #     print()

    # 2 for the enclosing "
    # count the single \ which are escaped like so \\
    # count all the " which includes the beginning and end of a string
    result = sum(2 + _.count('\\') + _.count('"') for _ in f)
    print(
        f"Answer to puzzle 2: {result}")
