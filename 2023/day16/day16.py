'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/16
'''


# input from website
from copy import deepcopy
sample_input = False
input = 'day16_sample.txt' if sample_input else 'day16.txt'
with open(input, 'r') as f:
    data = [[x for x in y]
            for y in f.read().splitlines()]


def find_energized_tiles(starting_position, starting_direction, layout, print_layout=False):
    layout_max_x = len(layout[0])
    layout_max_y = len(layout)

    energized_tiles = {}
    directions = {
        "down": (0, 1),
        "up": (0, -1),
        "left": (-1, 0),
        "right": (1, 0),
    }
    horizontal = ["left", "right"]
    vertical = ["up", "down"]
    started_rays = set()

    def start_ray(position, direction):
        while True:
            energized_tiles[(position[1], position[0])] = 1
            match layout[position[1]][position[0]]:
                case ".":
                    pass
                case "|":
                    if direction in horizontal:
                        if (position, "up") not in started_rays:
                            started_rays.add((position, "up"))
                            start_ray(position, "up")
                        if (position, "down") not in started_rays:
                            started_rays.add((position, "down"))
                            start_ray(position, "down")
                        break
                    else:
                        pass
                case "-":
                    if direction in vertical:
                        if (position, "left") not in started_rays:
                            started_rays.add((position, "left"))
                            start_ray(position, "left")
                        if (position, "right") not in started_rays:
                            started_rays.add((position, "right"))
                            start_ray(position, "right")
                        break
                    else:
                        pass
                case "\\":
                    if direction == "right":
                        direction = "down"
                    elif direction == "left":
                        direction = "up"
                    elif direction == "up":
                        direction = "left"
                    else:
                        direction = "right"
                case "/":
                    if direction == "right":
                        direction = "up"
                    elif direction == "left":
                        direction = "down"
                    elif direction == "up":
                        direction = "right"
                    else:
                        direction = "left"

            x = position[0] + directions[direction][0]
            y = position[1] + directions[direction][1]
            if x < 0 or x > layout_max_x-1 or y < 0 or y > layout_max_y-1:
                break
            position = (x, y)

    start_ray(starting_position, starting_direction)

    if print_layout:
        for line in layout:
            print("".join(line))
        print()
        for y, line in enumerate(layout):
            for x, c in enumerate(line):
                if (y, x) in energized_tiles:
                    print("#", end="")
                else:
                    print(c, end="")
            print()
        print()

    return sum(energized_tiles.values())


# part 1
print(find_energized_tiles((0, 0), "right", data))


different_starting_combinations = []
for x in range(len(data[0])):
    different_starting_combinations.append(
        find_energized_tiles((x, 0), "down", data))
    different_starting_combinations.append(
        find_energized_tiles((x, len(data)-1), "up", data))

for y in range(len(data)):
    different_starting_combinations.append(
        find_energized_tiles((0, y), "right", data))
    different_starting_combinations.append(
        find_energized_tiles((len(data[0])-1, y), "left", data))

# part 2
print(max(different_starting_combinations))
