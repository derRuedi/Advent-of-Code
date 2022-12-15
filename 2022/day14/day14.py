'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/14
'''

from termcolor import colored

# input from website
sample_input = True
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = [line.split(" -> ") for line in f.read().splitlines()]

source = (500, 0)

xs = []
ys = []

for p in data:
    for k in p:
        x, y = k.split(",")
        xs.append(int(x))
        ys.append(int(y))


min_x = min(xs)
max_x = max(xs)

min_y = min(ys)
max_y = max(ys)

print("min_x", min_x)
print("max_x", max_x)

print("min_y", min_y)
print("max_y", max_y)


def print_matrix(matrix):
    for i, line in enumerate(matrix):
        print(
            f"{i}\t{' '.join([l if l != '#' else colored('#', 'red', attrs=['bold'])for l in line])}")


def draw_line(paths):
    for i in range(len(paths)-1):
        x1, y1 = list(map(int, paths[i].split(",")))
        x2, y2 = list(map(int, paths[i+1].split(",")))

        start_x = min(x1, x2)
        stop_x = max(x1, x2)

        start_y = min(y1, y2)
        stop_y = max(y1, y2)

        x, y = 0, 0
        if start_x == stop_x:
            y = 1
        else:
            x = 1

        for j in range(max(abs(stop_x-start_x), abs(stop_y-start_y))+1):
            matrix[start_y + y*j][start_x + x*j - min_x] = "#"


# initialize matrix
matrix = [["." for x in range(max(xs) - min(xs) + 1)]
          for y in range(max(ys) + 1)]

# add sand source
matrix[source[1]][source[0] - min(xs)] = "+"

# add horizontal and vertical lines according to input data
for paths in data:
    draw_line(paths)

# print matrix
# print_matrix(matrix)

# drop sand
count = 0
stop = False
while not stop:
    sand_position = list(source)
    moving_possible = True
    while moving_possible:
        current_x, current_y = sand_position
        down = (current_x, current_y + 1)
        left_down = (current_x - 1, current_y+1)
        right_down = (current_x + 1, current_y + 1)
        if down[1] > len(matrix) - 1:
            stop = True
            break
        if matrix[down[1]][down[0] - min_x] == ".":
            sand_position = down
        elif matrix[left_down[1]][left_down[0] - min_x] == ".":
            sand_position = left_down
        elif matrix[right_down[1]][right_down[0] - min_x] == ".":
            sand_position = right_down
        else:
            matrix[sand_position[1]][sand_position[0] - min_x] = "o"
            moving_possible = False
    count += 1

# print matrix
print_matrix(matrix)

print(count-1)
