'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/10
'''
from termcolor import colored
from icecream import ic

# input from website
sample_input = False
input = 'day10_sample.txt' if sample_input else 'day10.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def print_grid_colored(grid, highlight_points=None):
    xmin, *_, xmax = sorted({x for x, y in grid.keys()})
    ymin, *_, ymax = sorted({y for x, y in grid.keys()})
    print()
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if highlight_points and (x, y) in highlight_points:
                print(colored(grid.get((x, y), " "),
                      "red", attrs=["bold"]), end="")
            else:
                print(grid.get((x, y), " "), end="")
        print()
    print()


def find_points(grid, char):
    points = []
    for p, c in grid.items():
        if char == c:
            points.append(p)
    return points


def find_hiking_trails(trailhead):
    hiking_trails = [[trailhead]]
    neighbors_to_check = {
        (-1, 0),  # left
        (+1, 0),  # right
        (0, -1),  # up
        (0, +1)  # down
    }
    for i in range(9):
        new_hiking_trails = []
        for trail in hiking_trails:
            current_position = trail[-1]
            possible_moves = []
            for neighbor in neighbors_to_check:
                check = (current_position[0] + neighbor[0],
                         current_position[1] + neighbor[1])
                if check in grid and grid[check].isdigit() and int(grid[check]) == int(grid[current_position]) + 1:
                    possible_moves.append(check)
            for pm in possible_moves:
                new_trail = trail[:]
                new_trail.append(pm)
                new_hiking_trails.append(new_trail)
        hiking_trails = new_hiking_trails
    return hiking_trails


grid = {(x, y): char
        for y, line in enumerate(data)
        for x, char in enumerate(line)}

xmin, *_, xmax = sorted({x for x, y in grid.keys()})
ymin, *_, ymax = sorted({y for x, y in grid.keys()})

trailheads = find_points(grid, "0")
end_points = find_points(grid, "9")
ic(trailheads)


def calculate_trailhead_score(trails):
    unique_start_end_trails = []
    for trail in trails:
        start_end = (trail[0], trail[-1])
        if start_end not in unique_start_end_trails:
            unique_start_end_trails.append(start_end)
    return len(unique_start_end_trails)


def calculate_trailhead_rating(trails):
    return len(trails)


sum_trailhead_scores = 0
sum_trailhead_ratings = 0
for th in trailheads:
    hiking_trails = find_hiking_trails(th)
    sum_trailhead_scores += calculate_trailhead_score(hiking_trails)
    sum_trailhead_ratings += calculate_trailhead_rating(hiking_trails)

print(f"puzzle 1: {sum_trailhead_scores}")
print(f"puzzle 2: {sum_trailhead_ratings}")
