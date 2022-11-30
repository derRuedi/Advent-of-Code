'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


button = 5
code = ""

for line in data:
    for move in line:
        match move:
            case "U":
                if button - 3 >= 1:
                    button = button - 3
            case "D":
                if button + 3 <= 9:
                    button = button + 3
            case "L":
                if button not in [1, 4, 7]:
                    button = button - 1
            case "R":
                if button not in [3, 6, 9]:
                    button = button + 1
    code += str(button)

print("The bathroom code is:", code)


button = "5"
code = ""
allowed_moves = {
    "1": {"D": "3"},
    "2": {"D": "6", "R": "3"},
    "3": {"U": "1", "R": "4", "D": "7", "L": "2"},
    "4": {"L": "3", "D": "8"},
    "5": {"R": "6"},
    "6": {"U": "2", "R": "7", "D": "A", "L": "5"},
    "7": {"U": "3", "R": "8", "D": "B", "L": "6"},
    "8": {"U": "4", "R": "9", "D": "C", "L": "7"},
    "9": {"L": "8"},
    "A": {"U": "6", "R": "B"},
    "B": {"U": "7", "R": "C", "D": "D", "L": "A"},
    "C": {"U": "8", "L": "B"},
    "D": {"U": "B"},
}

for line in data:
    for move in line:
        if move in allowed_moves[button]:
            button = allowed_moves[button][move]
    code += button

print("The bathroom code is:", code)
