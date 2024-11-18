'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

from itertools import permutations
from collections import deque
import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()

initial_password = "abcdefgh"

use_sample_input = False
if use_sample_input:
    data = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
""".splitlines()
    initial_password = "abcde"


def scrambling(operation: str, password: deque) -> deque:
    match operation.split(" "):
        case ["swap", "position" | "letter", *_] as instruction:
            if instruction[1] == "letter":
                x = int(password.index(instruction[2]))
                y = int(password.index(instruction[5]))
            else:
                x = int(instruction[2])
                y = int(instruction[-1])
            tmp = password[x]
            password[x] = password[y]
            password[y] = tmp
            return password
        case ["rotate", "left" | "right", *_] as instruction:
            if instruction[1] == "left":
                direction = -1
            else:
                direction = 1
            steps = int(instruction[-2]) * direction
            password.rotate(steps)
            return password
        case ["rotate", "based", *_] as instruction:
            steps = 0
            index_before = int(password.index(instruction[-1]))
            password.rotate(1)
            index_after = int(password.index(instruction[-1]))
            if index_before >= 4:
                steps += 1
            steps += index_after - 1
            password.rotate(steps)
            return password
        case ["reverse", *_] as instruction:
            x = int(instruction[2])
            y = int(instruction[-1])
            # if x == 0 and y == len(password)-1:
            #     return reversed(password)
            tmp_password = list(password)
            leading, reverse, trailing = \
                tmp_password[:x], tmp_password[x:y+1], tmp_password[y+1:]
            reverse.reverse()
            return deque(leading + reverse + trailing)
        case ["move", *_] as instruction:
            x = int(instruction[2])
            y = int(instruction[-1])
            tmp = password[x]
            password.remove(tmp)
            password.insert(y, tmp)
            return password
        case _:
            print("IN HERE- NOOOO!"*100)
            pass
    return password


assert list("ebcda") == list(scrambling(
    "swap position 4 with position 0", deque("abcde")))
assert list("edcba") == list(scrambling(
    "swap letter d with letter b", deque("ebcda")))
assert list("abcde") == list(scrambling(
    "reverse positions 0 through 4", deque("edcba")))
assert list("bcdea") == list(scrambling(
    "rotate left 1 step", deque("abcde")))
assert list("bdeac") == list(scrambling(
    "move position 1 to position 4", deque("bcdea")))
assert list("abdec") == list(scrambling(
    "move position 3 to position 0", deque("bdeac")))
assert list("ecabd") == list(scrambling(
    "rotate based on position of letter b", deque("abdec")))
assert list("decab") == list(scrambling(
    "rotate based on position of letter d", deque("ecabd")))


def scrambling_password(initial_password):
    password = deque(initial_password)
    for instruction in data:
        password = scrambling(instruction, password)
    return password


# part 1
print("".join(scrambling_password(initial_password)))

# part 2
scrambled_password = "fbgdceah"
for every_possible_password in ["".join(epp) for epp in permutations(scrambled_password)]:
    if "".join(scrambling_password(every_possible_password)) == scrambled_password:
        print("".join(every_possible_password))
        break
