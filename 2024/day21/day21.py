'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/21
'''

from itertools import permutations
import functools

# input from website
sample_input = False
input = 'day21_sample.txt' if sample_input else 'day21.txt'
with open(input, 'r') as f:
    codes = f.read().splitlines()

numeric_keypad = {n: (x, y) for y, line in enumerate(
    """789
456
123
 0A""".splitlines()) for x, n in enumerate(line) if n != " "}

directional_keypad = {n: (x, y) for y, line in enumerate(
    """ ^A
<v>""".splitlines()) for x, n in enumerate(line) if n != " "}

directions = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


@functools.lru_cache(maxsize=None)
def count_presses(code, robots, numeric, current_position):
    if numeric:
        keypad = numeric_keypad
    else:
        keypad = directional_keypad

    # no code, no sequence, no presses
    if not code:
        return 0

    # All robots will initially aim at the keypad's A key, wherever it is.
    if not current_position:
        current_position = keypad["A"]

    current_x, current_y = current_position
    destination_x, destination_y = keypad[code[0]]

    # keypad["A"] will always be in the lower right, thus max x and y value
    dx, dy = destination_x-current_x, destination_y-current_y

    # how to get to the destination position
    # order does not matter, ">>vv" will reach the destination as well as ">v>v"
    # we will deal with the (shortest) order later
    seq = dx*">" + \
        (abs(dx)*"<" if dx < 0 else "") + \
        dy*"v" + \
        (abs(dy)*"^" if dy < 0 else "")

    if robots:
        order_lengths = []
        for various_order in set(permutations(seq)):
            current_x, current_y = current_position
            for destination in various_order:
                dx, dy = directions[destination]
                current_x += dx
                current_y += dy
                # if a robot arm is ever aimed at a gap where no button is present on the keypad,
                # even for an instant, the robot will panic unrecoverably
                # don't do that
                if (current_x, current_y) not in keypad.values():
                    break
            else:

                order_lengths.append(count_presses(
                    various_order+('A', ), robots - 1, False, None))
        minimal_order_length = min(order_lengths)
    else:
        minimal_order_length = len(seq) + 1
    return minimal_order_length + count_presses(code[1:], robots, numeric, (destination_x, destination_y))


puzzle_1 = 0
for code in codes:
    puzzle_1 += count_presses(code, 2, True, None) * int(code[:-1])
print(puzzle_1)

puzzle_2 = 0
for code in codes:
    puzzle_2 += count_presses(code, 25, True, None) * int(code[:-1])
print(puzzle_2)
