'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/23
'''

from collections import deque
from collections import Counter

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

elves = {(x, y) for y, line in enumerate(data)
         for x, char in enumerate(line) if char == "#"}

directions = deque([
    (0, -1),  # north
    (0, +1),  # south
    (-1, 0),  # west
    (+1, 0),  # east
])

adjacent = {(x, y)
            for y in range(-1, 2)
            for x in range(-1, 2)
            if not (x == 0 and y == 0)}


def print_elves(elves):
    empty_tiles = 0
    xs = [e[0] for e in elves]
    ys = [e[1] for e in elves]

    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            print("#" if (x, y) in elves else ".", end="")
            if (x, y) not in elves:
                empty_tiles += 1
        print()
    print()

    return empty_tiles


for round in range(100_000):

    elves_and_moves = []
    elves_after_round = set()
    for elf in elves:
        move = next(
            ((elf[0] + direction[0], elf[1] + direction[1]) for direction in directions
             # if there is an elf adjacent to the current elf, consider moving, otherwise the elf does not do anything during this round
             if any((elf[0] + a[0], elf[1] + a[1]) in elves for a in adjacent)
             # if the elf considers moving,
             # the elf looks in each of the four directions (in the current order) and proposes moving one step in the first valid direction
             # depending on the direction you are currently facing, check the adjacent left, middle and right field
             # if it is free, consider this as the next move, otherwise check for the following direction
                and not any(
                    (elf[0] + direction[0] + direction[1]*direction_offset,
                     elf[1] + direction[1] + direction[0]*direction_offset)
                    in elves for direction_offset in (-1, 0, +1))),
            None)
        if move:
            # possible move, needs to be checked
            elves_and_moves.append([elf, move])
        else:
            # if an elf does not move, it stays where it is
            elves_after_round.add(elf)

    all_moves = [move for _, move in elves_and_moves]
    all_moves_counted = Counter(all_moves)
    moves_to_remove = {
        move for move in all_moves if all_moves_counted[move] > 1 and move != None}

    if not all_moves:
        print(round+1)
        break

    for elf, move in elves_and_moves:
        if move in moves_to_remove:
            elves_after_round.add(elf)
        else:
            elves_after_round.add(move)

    assert len(elves) == len(elves_after_round)
    # all new positions
    elves = elves_after_round

    # the first direction the Elves considered is moved to the end of the list of directions
    directions.rotate(-1)

print(print_elves(elves))
