'''
    Advent of Code Day 9
    https://adventofcode.com/2021/day/9
'''

data = []
with open("day9.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]


def process_input_data(data):
    new_data = []
    for line in data:
        new_data.append([int(i) for i in line])
    return new_data


def find_low_points(heightmap):
    low_points = []
    neighbors_to_check = {
        "left": (-1, 0),
        "right": (+1, 0),
        "above": (0, -1),
        "below": (0, +1)
    }

    for x in range(len(heightmap[0])):
        for y in range(len(heightmap)):
            pos_value = heightmap[y][x]
            add_point_as_low_point = []
            for neighbor in neighbors_to_check.values():
                check_x = x + neighbor[0]
                check_y = y + neighbor[1]
                if check_x < 0 or check_x >= len(heightmap[0]) or check_y < 0 or check_y >= len(heightmap):
                    continue
                point_value = heightmap[check_y][check_x]
                add_point_as_low_point.append(pos_value < point_value)
            if all(add_point_as_low_point):
                low_points.append((x, y))
    return low_points


def check_surrounding_points(heightmap, point):
    x = point[0]
    y = point[1]
    pos_value = heightmap[y][x]
    neighbors_to_check = {
        "left": (-1, 0),
        "right": (+1, 0),
        "above": (0, -1),
        "below": (0, +1)
    }
    basin = []
    for neighbor in neighbors_to_check.values():
        check_x = x + neighbor[0]
        check_y = y + neighbor[1]
        if check_x < 0 or check_x >= len(heightmap[0]) or check_y < 0 or check_y >= len(heightmap):
            continue
        point_value = heightmap[check_y][check_x]
        if point_value != 9 and point_value > pos_value:
            point_to_add = (check_x, check_y)
            basin.append(point_to_add)
            basin.extend(check_surrounding_points(heightmap, point_to_add))
    return basin


def puzzle1(data):
    heightmap = process_input_data(data)
    low_points = find_low_points(heightmap)
    values_low_points = [heightmap[y][x] for x, y in low_points]
    return sum((i+1 for i in values_low_points))


def puzzle2(data):
    heightmap = process_input_data(data)
    low_points = find_low_points(heightmap)
    basins_size = []
    for low_point in low_points:
        basin = check_surrounding_points(heightmap, low_point)
        basin.append(low_point)
        unique_basin_points = set()
        for point in basin:
            unique_basin_points.add(point)
        basins_size.append(len(unique_basin_points))
    basins_size.sort()
    return basins_size[-1] * basins_size[-2] * basins_size[-3]


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
