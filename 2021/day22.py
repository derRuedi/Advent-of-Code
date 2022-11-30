'''
    Advent of Code Day 22
    https://adventofcode.com/2021/day/22
'''

from itertools import combinations


def process_input_data(filename):
    data = []
    with open(filename, "r") as f:
        data = f.read().splitlines()
    cuboids = []
    for line in data:
        status, coordinates = line.split()
        x, y, z = coordinates.split(",")
        x_start, x_end = x[2:].split("..")
        y_start, y_end = y[2:].split("..")
        z_start, z_end = z[2:].split("..")
        cuboid = {
            "status": status,
            "x": (int(x_start), int(x_end)),
            "y": (int(y_start), int(y_end)),
            "z": (int(z_start), int(z_end)),
        }
        if not (cuboid["x"][0] < -50 or cuboid["x"][1] > 50
                or cuboid["y"][0] < -50 or cuboid["y"][1] > 50
                or cuboid["z"][0] < -50 or cuboid["z"][1] > 50):
            cuboids.append(cuboid)
    return cuboids


def puzzle1(filename):
    perm = {}

    cuboids = process_input_data(filename)
    for cuboid in cuboids:
        x_range = list(range(cuboid["x"][0], cuboid["x"][1]+1))
        y_range = list(range(cuboid["y"][0], cuboid["y"][1]+1))
        z_range = list(range(cuboid["z"][0], cuboid["z"][1]+1))

        for x in list(range(cuboid["x"][0], cuboid["x"][1]+1)):
            for y in list(range(cuboid["y"][0], cuboid["y"][1]+1)):
                for z in list(range(cuboid["z"][0], cuboid["z"][1]+1)):
                    perm[f"{x},{y},{z}"] = cuboid["status"]

    result = [1 for v in perm.values() if v == "on"]
    return len(result)


def puzzle2(filename):
    pass


if __name__ == "__main__":
    pass
    # assertions go here

    print(
        f"The answer to Puzzle #1's sample data is: {puzzle1('day22.sample_input.txt')}")
    print(f"The answer to Puzzle #1 is: {puzzle1('day22.input.txt')}")

    # print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
    # print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
