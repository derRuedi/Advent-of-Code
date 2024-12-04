'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/4
'''

# input from website
import re
sample_input = False
input = 'day4_sample.txt' if sample_input else 'day4.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def print_grid(grid: dict):
    print("\n".join("".join(grid.get((x, y), ' ')
          for x in range(xmin, xmax + 1)) for y in range(ymin, ymax + 1)))


grid = {(x, y): char
        for y, line in enumerate(data)
        for x, char in enumerate(line)}

xmin, *_, xmax = sorted({x for x, y in grid.keys()})
ymin, *_, ymax = sorted({y for x, y in grid.keys()})

# print_grid(grid)

word_search = "XMAS"
directions = [
    (0, -1),  # up
    (1, -1),  # up    right
    (1, 0),  # right
    (1, 1),   # down  right
    (0, 1),   # down
    (-1, 1),  # down  left
    (-1, 0),  # left
    (-1, -1),  # up    left
]

contenders = []
for y in range(xmax+1):
    for x in range(ymax+1):
        x_offset = x
        y_offset = y
        for dir_x, dir_y in directions:
            word = [grid.get((x, y), '#')]
            for i in range(len(word_search)-1):
                char = grid.get((x_offset + dir_x * (i+1),
                                 y_offset + dir_y * (i+1)),
                                ' ')
                word.append(char)
            contenders.append("".join(word))

print(f"puzzle 1: {
      len([c for c in contenders if c == word_search])}")


contenders = []
three_by_three = [
    # 1 2 3
    # 4 5 6
    # 7 8 9
    (0, 0),  # 1
    (1, 0),  # 2
    (2, 0),  # 3
    (0, 1),  # 4
    (1, 1),  # 5
    (2, 1),  # 6
    (0, 2),  # 7
    (1, 2),  # 8
    (2, 2)  # 9
]

for y in range(xmax+1):
    for x in range(ymax+1):
        word = []
        for point in three_by_three:
            char = grid.get((x + point[0], y+point[1]), ' ')
            word.append(char)
        contenders.append("".join(word))

# patterns for X-MAS:
# M.S   S.S   S.M   M.M
# .A.   .A.   .A.   .A.
# M.S   M.M   S.M   S.S
regex = r"(M.S.A.M.S)|(S.S.A.M.M)|(S.M.A.S.M)|(M.M.A.S.S)"
print(f"puzzle 2: {
      len([c for c in contenders if re.match(regex, c)])}")
