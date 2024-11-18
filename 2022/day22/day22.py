'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/22
'''

import re
from termcolor import colored

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    matrix, path = f.read().split("\n\n")
    matrix = matrix.splitlines()
    path = re.findall("[0-9]+|[LR]", path)

directions = [
    (+1, 0),  # right
    (0, +1),  # "down" in terms of going down in graph but down in graph is up in y
    (-1, 0),  # left
    (0, -1),  # "up" in terms of going up in graph but up in graph is down in y
]
horizontal_directions = [directions[0], directions[2]]
vertical_directions = [directions[1], directions[3]]


def change_direction(cur_dir, direction):
    return directions[(directions.index(cur_dir) + (1 if direction == "R" else -1)) % len(directions)]


def print_matrix(matrix, highlight_points=None):
    print()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if (x, y) in highlight_points:
                print(colored(matrix[y][x], "red", attrs=["bold"]), end="")
            else:
                print(matrix[y][x], end="")
        print()
    print()


def starting_position(matrix):
    x = 0
    while matrix[0][x] == " ":
        x += 1
    return [x, 0]


current_position = starting_position(matrix)
# current_position = [8, 0]
visited_positions = [tuple(current_position)]


# initial direction is "right"
direction = (1, 0)

# print_matrix(matrix, visited_positions)

print(path)
print()

for cmd in path:
    if cmd.isdigit():
        steps = int(cmd)
        for _ in range(steps):
            new_position = [current_position[0] + direction[0],
                            current_position[1] + direction[1]]
            # direction is horizontal
            if direction in horizontal_directions:
                blanks = matrix[new_position[1]].count(" ")
                # if we exceed the matrix
                # wrap around
                if new_position[0] > len(matrix[new_position[1]]) - 1:
                    new_position[0] = \
                        blanks + new_position[0] % len(matrix[new_position[1]])
                # if we hit the empty space to the left or the beginning of the array (blanks is equal to 0 if there is no empty space)
                # wrap around
                if new_position[0] < blanks:
                    new_position[0] = \
                        len(matrix[new_position[1]]) - blanks + new_position[0]

                # if the new position hits a road block
                # stop
                if matrix[new_position[1]][new_position[0]] == "#":
                    break

            # direction is vertical
            else:
                x = new_position[0]
                ys = []
                for y in range(len(matrix)):
                    try:
                        if matrix[y][x] != " ":
                            ys.append(y)
                    except IndexError:
                        pass
                min_y = min(ys)
                max_y = max(ys)

                # if we exceed the matrix
                # wrap around
                if new_position[1] > max_y:
                    new_position[1] = min_y
                # if we hit the empty space to the left or the beginning of the array (blanks is equal to 0 if there is no empty space)
                # wrap around
                if new_position[1] < min_y:
                    new_position[1] = max_y

                # if the new position hits a road block
                # stop
                if matrix[new_position[1]][new_position[0]] == "#":
                    break

            # if all is good
            # update current position and add it to visited positions
            current_position = new_position
            visited_positions.append(tuple(current_position))
    else:
        direction = change_direction(direction, cmd)

# rows start from 1 at the top and count downward
# columns start from 1 at the left and count rightward
row = current_position[1] + 1
column = current_position[0] + 1
facing = directions.index(direction)

print(1000 * row + 4 * column + facing)

print_matrix(matrix, visited_positions)
