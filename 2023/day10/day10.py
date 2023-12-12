'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/10
'''

import matplotlib.path
from termcolor import colored

# input from website
sample_input = False
input = 'day10_sample.txt' if sample_input else 'day10.txt'
with open(input, 'r') as f:
    data = [[x for x in y] for y in f.read().splitlines()]

directions = {
    "down": (0, 1),
    "up": (0, -1),
    "left": (-1, 0),
    "right": (1, 0),
}
horizontal = ["left", "right"]
vertical = ["up", "down"]

for y, line in enumerate(data):
    if "S" in line:
        S = (line.index("S"), y)


def find_loop(S, maze):
    for dir, (diff) in directions.items():
        if dir == "down" and maze[S[1]+diff[1]][S[0]+diff[0]] in ["|", "L", "J"]:
            break
        elif dir == "up" and maze[S[1]+diff[1]][S[0]+diff[0]] in ["|", "7", "F"]:
            break
        elif dir == "left" and maze[S[1]+diff[1]][S[0]+diff[0]] in ["-", "L", "F"]:
            break
        elif dir == "right" and maze[S[1]+diff[1]][S[0]+diff[0]] in ["-", "7", "J"]:
            break
        else:
            print(f"Could not start a loop from S{S}.")

    direction = dir
    position = (S[0]+diff[0], S[1]+diff[1])
    loop = [S, position]

    while True:
        match maze[position[1]][position[0]]:
            case "|" | "-":  # vertical
                pass
            case "L":  # up, right
                if direction == "left":
                    direction = "up"
                elif direction == "down":
                    direction = "right"
            case "J":  # up, left
                if direction == "right":
                    direction = "up"
                elif direction == "down":
                    direction = "left"
            case "7":  # up, left
                if direction == "right":
                    direction = "down"
                elif direction == "up":
                    direction = "left"
            case "F":  # up, right
                if direction == "left":
                    direction = "down"
                elif direction == "up":
                    direction = "right"
            case ".":  # no pipe
                print(
                    f"no pipe here {maze[position[1]][position[0]]} - {position}")
            case "S":  # animal
                print(
                    f"animal here {maze[position[1]][position[0]]} - {position}")

        x = position[0] + directions[direction][0]
        y = position[1] + directions[direction][1]
        position = (x, y)
        if position in loop:
            break
        loop.append(position)
    return loop


def print_matrix(matrix, path=[], enclosed_points=[]):
    inside = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if (x, y) in path:
                better_display = {"F": "┌", "L": "└", "7": "┐",
                                  "J": "┘", "|": "│", "-": "─", "S": "┼", ".": " "}
                print(colored(better_display[matrix[y][x]],
                      "red", attrs=["bold"]), end="")
            elif (x, y) in enclosed_points:
                print(colored("•", "blue", attrs=["bold"]), end="")
            else:
                print(".", end="")
        print()
    print()


loop = find_loop(S, data)
# print_matrix(data, loop)
print(len(loop) // 2)

# Jordan curve theorem
inside_points = []
polygon = matplotlib.path.Path(loop)
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) not in loop and polygon.contains_point((x, y)):
            inside_points.append((x, y))

print(len(inside_points))

print_matrix(data, loop, inside_points)
