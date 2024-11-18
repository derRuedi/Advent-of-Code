'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/14
'''

from termcolor import colored

# input from website
sample_input = False
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

part_2 = True
print_part1 = False
print_part2 = False

# add "infinite" floor (it just needs to "hold" the pyramid of sand --> "height of the pyramid x 2 - 1")
if part_2:
    floor_x = (max(ys) + 2) * 2 - 1
    floor_y = max(ys) + 2
    data.append([f"{500-floor_x//2-1},{floor_y}",
                f"{500+floor_x//2+1},{floor_y}"])
    xs.append(500-floor_x//2-1)
    xs.append(500+floor_x//2+1)
    ys.append(floor_y)

min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)


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

        for j in range(max(stop_x-start_x, stop_y-start_y)+1):
            matrix[start_y + y*j][start_x + x*j - min_x] = "#"


# initialize matrix
matrix = [["." for x in range(max(xs) - min(xs) + 1)]
          for y in range(max(ys) + 1)]

# add sand source
matrix[source[1]][source[0] - min(xs)] = "+"

# add horizontal and vertical lines according to input data
for paths in data:
    draw_line(paths)


# drop sand
count = 0
stop = False
part1_solved = False
while not stop:
    sand_position = list(source)
    moving_possible = True
    while moving_possible:
        current_x, current_y = sand_position
        down = (current_x, current_y + 1)
        left_down = (current_x - 1, current_y+1)
        right_down = (current_x + 1, current_y + 1)
        if not part1_solved and down[1] > max_y - 2:
            part1_solved = True
            if print_part1:
                print_matrix(matrix)
            result_part1 = count
            if not part_2:
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
            if sand_position == list(source):
                stop = True
                result_part2 = count + 1
                if print_part2:
                    print_matrix(matrix)
                break
            moving_possible = False
    count += 1


print("result part 1:", result_part1)
print("result part 2:", result_part2)
