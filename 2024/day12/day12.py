'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/12
'''

from termcolor import colored
from icecream import ic

# input from website
sample_input = False
input = 'day12_sample.txt' if sample_input else 'day12.txt'
with open(input, 'r') as f:
    data = [[x for x in y] for y in f.read().splitlines()]


def print_matrix(matrix, highlight_points=None):
    colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan"]
    print()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if type(highlight_points) == list and type(highlight_points[0]) == list:
                if (x, y) in [item for sublist in highlight_points for item in sublist]:
                    for idx, hp in enumerate(highlight_points):
                        if (x, y) in hp:
                            print(colored(matrix[y][x], colors[idx % len(
                                colors)], attrs=["bold"]), end="")
                else:
                    print(matrix[y][x], end="")
            else:
                if highlight_points and ((x, y) in highlight_points or [x, y] in highlight_points):
                    print(colored(matrix[y][x], "red", attrs=["bold"]), end="")
                else:
                    print(matrix[y][x], end="")
        print()
    print()


def total_fence_price(grid, bulk=False):
    n = len(grid[0])  # x-axis
    m = len(grid)  # y-axis
    visited = [[False for x in y] for y in grid]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def find_neighbors(x, y):
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:  # check boundaries
                neighbors.append((nx, ny))
        return neighbors

    def explore_region_perimeter(x, y, plant_type):
        stack = [(x, y)]
        visited[y][x] = True
        area = 0
        perimeter = 0
        region = set()

        while stack:
            cx, cy = stack.pop()
            area += 1
            region.add((cx, cy))
            for nx, ny in find_neighbors(cx, cy):
                if grid[ny][nx] == plant_type and not visited[ny][nx]:
                    visited[ny][nx] = True
                    stack.append((nx, ny))
                elif grid[ny][nx] != plant_type:  # edge contributes to perimeter
                    perimeter += 1
            # if on the edge of the grid, count edge as perimeter
            if cx == 0 or cx == n-1:
                perimeter += 1
            if cy == 0 or cy == m-1:
                perimeter += 1

        return area, perimeter, region

    total_price = 0
    regions = []
    for y in range(m):
        for x in range(n):
            if not visited[y][x]:
                plant_type = grid[y][x]
                area, perimeter, region = explore_region_perimeter(
                    x, y, plant_type)
                total_price += area * perimeter
                regions.append(list(region))

    # print_matrix(grid, regions)

    if not bulk:
        return total_price
    else:
        total_price = 0

        # initial solution did not work, so just go over every region and fuck it
        for region in regions:
            area = len(region)

            seen = set()
            corners = 0

            for row, col in region:
                for dx, dy in [
                    (-0.5, -0.5),
                    (0.5, -0.5),
                    (0.5, 0.5),
                    (-0.5, 0.5),
                ]:
                    new_row = row + dx
                    new_col = col + dy

                    if (new_row, new_col) in seen:
                        continue

                    seen.add((new_row, new_col))

                    adjacent = sum(
                        (new_row + r, new_col + c) in region
                        for r, c in [
                            (-0.5, -0.5),
                            (0.5, -0.5),
                            (0.5, 0.5),
                            (-0.5, 0.5),
                        ]
                    )

                    if adjacent == 1 or adjacent == 3:
                        corners += 1
                    elif adjacent == 2:
                        # diagonal
                        pattern = [
                            (r, c) in region
                            for r, c in [
                                (new_row - 0.5, new_col - 0.5),
                                (new_row + 0.5, new_col + 0.5),
                            ]
                        ]

                        if pattern == [True, True] or pattern == [False, False]:
                            corners += 2

            total_price += area * corners

    return total_price


print(total_fence_price(data))
print(total_fence_price(data, True))
