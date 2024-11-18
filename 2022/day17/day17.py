'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/17
'''

from termcolor import colored

# input from website
sample_input = True
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read()


def infinite_jet_pattern(pattern: list):
    i = 0
    while True:
        yield -1 if pattern[i % len(pattern)] == "<" else 1
        i += 1


def infinite_rock_shapes(upper_bound=0):
    i = 0
    # rocks = [
    #     [['#', '#', '#', '#']],
    #     [['.', '#', '.'],
    #      ['#', '#', '#'],
    #      ['.', '#', '.']
    #      ],
    #     [['.', '.', '#'],
    #      ['.', '.', '#'],
    #      ['#', '#', '#']],
    #     [['#'],
    #      ['#'],
    #      ['#'],
    #      ['#']],
    #     [['#', '#'],
    #      ['#', '#']]
    # ]
    rocks = [
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (1, 0), (0, 1), (1, 1))
    ]
    while True:
        yield rocks[i % len(rocks)]
        i += 1
        if upper_bound and i > upper_bound:
            break


def pyroclastic_flow():
    jet_pattern = infinite_jet_pattern(list(data))
    rock_pattern = infinite_rock_shapes()
    matrix = {(x, 0) for x in range(7)}
    top = 0
    offset_x = 2
    offset_y = 4

    def move(rock, direction, amount):
        if direction not in ["x", "y"]:
            print("'direction' must be 'x' or 'y'")
            return -1
        if direction == "x":
            direction = 0
        else:
            direction = 1
        for idx in range(len(rock)):
            rock[idx][direction] += amount

    def move_possible(rock, matrix, dx, dy):
        for idx in range(len(rock)):
            if not 0 <= rock[idx][0]+dx <= 6:
                return False
        for x, y in rock:
            if (x+dx, y+dy) in matrix:
                return False
        return True

    def remove_low_points(matrix, top):
        points_to_remove = [p for p in matrix if p[1] < top - 50]
        for p in points_to_remove:
            matrix.remove(p)

    part_1 = 2022
    part_2 = 1_000_000_000_000
    rounds = part_1
    for _ in range(rounds):
        rock = [[x+offset_x, y+offset_y+top] for x, y in next(rock_pattern)]

        while True:
            direction = next(jet_pattern)
            if move_possible(rock, matrix, direction, 0):
                move(rock, "x", direction)
            if move_possible(rock, matrix, 0, -1):
                move(rock, "y", -1)
            else:
                break
        top = max(max(y for x, y in rock), top)
        matrix.update({(x, y) for x, y in rock})

        # keep memory consumption low
        remove_low_points(matrix, top)
    print(top)


pyroclastic_flow()
