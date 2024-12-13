'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/6
'''

from termcolor import colored
from icecream import ic

# input from website
sample_input = False
input = 'day6_sample.txt' if sample_input else 'day6.txt'
with open(input, 'r') as f:
    data = [[x for x in y] for y in f.read().splitlines()]


def print_matrix(matrix, highlight_points=None):
    print()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if highlight_points and (x, y) in highlight_points:
                print(colored(matrix[y][x], "red", attrs=["bold"]), end="")
            else:
                print(matrix[y][x], end="")
        print()
    print()


def find_start(matrix, start_character):
    for y, line in enumerate(data):
        if start_character in line:
            start = (line.index(start_character), y)
    return start


def change_direction(cur_dir, direction="R"):
    directions = [
        (+1, 0),  # right
        (0, +1),  # "down" in terms of going down in graph but down in graph is up in y
        (-1, 0),  # left
        (0, -1),  # "up" in terms of going up in graph but up in graph is down in y
    ]
    return directions[(directions.index(cur_dir) + (1 if direction == "R" else -1)) % len(directions)]


def calculate_guard_route(matrix, starting_position, starting_direction):
    current_position = starting_position
    visited_positions = {current_position}
    direction = starting_direction

    x_min, x_max = 0, len(matrix[0]) - 1
    y_min, y_max = 0, len(matrix) - 1

    loop_count = 0

    while True:
        new_position = (current_position[0] + direction[0],
                        current_position[1] + direction[1])

        if not (x_min <= new_position[0] <= x_max and y_min <= new_position[1] <= y_max):
            break
        if matrix[new_position[1]][new_position[0]] == "#":
            direction = change_direction(direction)
            continue
        if new_position in visited_positions:
            # ic("I might be in a loop!")
            loop_count += 1
            if loop_count == 1000:
                return (visited_positions, True)
        visited_positions.add(tuple(new_position))
        current_position = new_position

    return (visited_positions, False)


# puzzle 1
starting_position = find_start(data, "^")
starting_direction = (0, -1)
guard_route, is_loop = calculate_guard_route(
    data, starting_position, starting_direction)
print_matrix(data, guard_route)
print(f"puzzle 1 {len(set(guard_route))}")

# puzzle 2
loop_points = set()
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] in "#^":
            continue
        data[y][x] = "#"

        starting_position = find_start(data, "^")
        starting_direction = (0, -1)
        guard_route, is_loop = calculate_guard_route(
            data, starting_position, starting_direction)
        if is_loop:
            loop_points.add((x, y))
        data[y][x] = "."

print(f"puzzle 2: {len(loop_points)}")
