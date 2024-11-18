'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/21
'''
from termcolor import colored
import numpy as np

# input from website
sample_input = False
input = 'day21_sample.txt' if sample_input else 'day21.txt'
with open(input, 'r') as f:
    data = [[c for c in line] for line in f.read().splitlines()]
puzzle_map = np.array(data)


def create_multiplied_map(puzzle_map, multiplier):
    if multiplier % 2 == 0:
        print("multiplier must be odd, will increase it for you")
        multiplier += 1
    return np.tile(puzzle_map, (multiplier, multiplier))


def print_matrix(matrix, path=[]):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if (y, x) in path:
                print(colored("O" if matrix[y][x] == "." else matrix[y][x],
                      "red", attrs=["bold"]), end="")
            else:
                print(matrix[y][x], end="")
        print()
    print()


def walk_steps(puzzle_map, steps):
    directions = (
        (1, 0),  # north
        (-1, 0),  # south
        (0, -1),  # east
        (0, 1),  # west
    )

    S = puzzle_map.shape
    S = (S[0]//2, S[1]//2)

    step_map = {S}
    for step in range(steps):
        check_for_new_steps = step_map.copy()
        step_map = set()
        try:

            for position in check_for_new_steps:
                for d in directions:
                    new_position = (position[0] + d[0], position[1] + d[1])
                    if puzzle_map[new_position[0]][new_position[1]] in ["S", "."]:
                        step_map.add(new_position)
        except IndexError:
            print(step)
            exit()

    # print_matrix(puzzle_map, step_map)
    return len(step_map)


# part 1
if sample_input:
    garden_plots_reached = walk_steps(puzzle_map, 6)
else:
    garden_plots_reached = walk_steps(puzzle_map, 64)
print("part 1 ", garden_plots_reached)


# part 2
x0 = walk_steps(puzzle_map, 65)

# need a bigger map
new_map = create_multiplied_map(puzzle_map, 5)
x1 = walk_steps(new_map, 65 + 131)
x2 = walk_steps(new_map, 65 + 131 + 131)


#
# Lagrange's Interpolation formula for ax^2 + bx + c with x=[0,1,2] and y=[y0,y1,y2] we have
#   f(x) = (x^2-3x+2) * y0/2 - (x^2-2x)*y1 + (x^2-x) * y2/2
# so the coefficients are:
# a = y0/2 - y1 + y2/2
# b = -3*y0/2 + 2*y1 - y2/2
# c = y0
#
def simplifiedLagrange(values):
    return {
        "a": values[0] / 2 - values[1] + values[2] / 2,
        "b": -3 * (values[0] / 2) + 2 * values[1] - values[2] / 2,
        "c": values[0]
    }


def polynomial(x, a, b, c):
    return x**2 * a + x * b + c


coefficients = simplifiedLagrange([x0, x1, x2])

x = 26501365 // 131
print(polynomial(x, *coefficients.values()))
