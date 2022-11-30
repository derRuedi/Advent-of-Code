'''
    Advent of Code Day 5
    https://adventofcode.com/2021/day/5
'''

data = []
with open("day5.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = []
with open("day5.sample_input.txt", "r") as f:
    sample_data = f.read().splitlines()


def process_input_data(data, strip_non_horizontal_or_vertical_lines=True):
    new_data = []
    for line in data:
        line = line.replace(" -> ", ",")
        x1, y1, x2, y2 = [int(i) for i in line.split(",")]
        if strip_non_horizontal_or_vertical_lines:
            if not ((x1 == x2) or (y1 == y2)):
                continue
        new_data.append({
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2
        })
    return new_data


def create_points(lines):
    points = []
    for line in lines:
        if line["x1"] == line["x2"]:
            y = min(line["y1"], line["y2"])
            y_max = max(line["y1"], line["y2"])
            while y <= y_max:
                points.append([line["x1"], y])
                y += 1
        elif line["y1"] == line["y2"]:
            x = min(line["x1"], line["x2"])
            x_max = max(line["x1"], line["x2"])
            while x <= x_max:
                points.append([x, line["y1"]])
                x += 1
        # following lines for the diagonals
        elif line["x1"] < line["x2"] and line["y1"] < line["y2"]:
            x = line["x1"]
            y = line["y1"]
            while x <= line["x2"] and y <= line["y2"]:
                points.append([x, y])
                x += 1
                y += 1
        elif line["x1"] > line["x2"] and line["y1"] > line["y2"]:
            x = line["x1"]
            y = line["y1"]
            while x >= line["x2"] and y >= line["y2"]:
                points.append([x, y])
                x -= 1
                y -= 1
        elif line["x1"] > line["x2"] and line["y1"] < line["y2"]:
            x = line["x1"]
            y = line["y1"]
            while x >= line["x2"] and y <= line["y2"]:
                points.append([x, y])
                x -= 1
                y += 1
        elif line["x1"] < line["x2"] and line["y1"] > line["y2"]:
            x = line["x1"]
            y = line["y1"]
            while x <= line["x2"] and y >= line["y2"]:
                points.append([x, y])
                x += 1
                y -= 1
        else:
            print(f"THIS IS SOME FREAKY POINT: {line}")
    return points


def create_board(points):
    w = max(x for x, y in points)
    h = max(y for x, y in points)
    board = [[0 for x in range(w+1)] for y in range(h+1)]
    for point in points:
        board[point[1]][point[0]] += 1
    return board


def calculate_dangerous_areas(data, ignore_diagonals=True):
    lines = process_input_data(data, ignore_diagonals)
    points = create_points(lines)
    board = create_board(points)

    dangerous_areas = 0
    for line in board:
        for num in line:
            if num >= 2:
                dangerous_areas += 1

    return dangerous_areas


def puzzle1(data):
    return calculate_dangerous_areas(data)


def puzzle2(data):
    return calculate_dangerous_areas(data, False)


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
