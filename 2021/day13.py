'''
    Advent of Code Day 13
    https://adventofcode.com/2021/day/13
'''

data = []
with open("day13.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5"
]


def process_input_data(data):
    folds = []
    points = []
    for line in data[0:data.index("")]:
        points.append([int(i) for i in line.split(",")])
    for line in data[data.index("")+1:]:
        folds.append(line.replace("fold along ", "").split("="))
    return folds, points


def create_and_fill_matrix(points):
    max_x = max((p[0] for p in points))
    max_y = max((p[1] for p in points))

    matrix = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]

    for p in points:
        matrix[p[1]][p[0]] = "#"

    return matrix


def fold(matrix, axis, value):
    if axis == "x":
        return foldX(matrix, value)
    elif axis == "y":
        return foldY(matrix, value)
    else:
        print(f"Invalid axis: {axis}. Axis can either be x or y.")
        return None


def foldX(matrix, value):
    m1 = [['.' for x in range(len(matrix[0])//2)] for y in range(len(matrix))]
    m2 = [['.' for x in range(len(matrix[0])//2)] for y in range(len(matrix))]
    m3 = [['.' for x in range(len(matrix[0])//2)] for y in range(len(matrix))]

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if x == value:
                continue
            elif x < value:
                m1[y][x] = matrix[y][x]
            elif x > value:
                x_reverse = value - 1 - (x % (value+1))
                m2[y][x_reverse] = matrix[y][x]

    for x in range(len(m1[0])):
        for y in range(len(m1)):
            if m1[y][x] == "#" or m2[y][x] == "#":
                m3[y][x] = "#"

    return m3


def foldY(matrix, value):
    m1 = [line for line in matrix[0:value]]
    m2 = [line for line in matrix[:value:-1]]
    m3 = [['.' for x in range(len(m1[0]))] for y in range(len(m1))]

    for x in range(len(m1[0])):
        for y in range(len(m1)):
            if m1[y][x] == "#" or m2[y][x] == "#":
                m3[y][x] = "#"

    return m3


def count_points(matrix, point_value="#"):
    return sum((line.count(point_value) for line in matrix))


def print_matrix(matrix):
    if matrix:
        for line in matrix:
            print("".join(line))
        print()


def puzzle1(data):
    folds, points = process_input_data(data)
    matrix = create_and_fill_matrix(points)

    m = matrix
    for f in folds[0:1]:
        m = fold(m, f[0], int(f[1]))

    return count_points(m)


def puzzle2(data):
    folds, points = process_input_data(data)
    matrix = create_and_fill_matrix(points)

    m = matrix
    for f in folds:
        m = fold(m, f[0], int(f[1]))

    print_matrix(m)


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print("The answer to Puzzle #2's sample data is:")
puzzle2(sample_data)
print("The answer to Puzzle #2 is:")
puzzle2(data)
