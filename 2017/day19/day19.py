'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/19
'''
import string
import time
from icecream import ic

# input from website
sample_input = False
input = 'day19_sample.txt' if sample_input else 'day19.txt'
with open(input, 'r') as f:
    data = [[x for x in y] for y in f.read().splitlines()]


letters = []
directions = {
    "down": (0, 1),
    "up": (0, -1),
    "left": (-1, 0),
    "right": (1, 0),
}
horizontal = ["left", "right"]
vertical = ["up", "down"]

position = (data[0].index("|"), 0)
direction = "down"

steps = 0

while True:
    match data[position[1]][position[0]]:
        case "|" | "-":
            pass
        case "+":
            if direction in vertical:
                if data[position[1]][position[0]-1] != " ":
                    direction = "left"
                else:
                    direction = "right"
            else:
                if data[position[1]-1][position[0]] != " ":
                    direction = "up"
                else:
                    direction = "down"
        case letter if data[position[1]][position[0]] in string.ascii_uppercase:
            letters.append(data[position[1]][position[0]])
        case " " | _:
            break

    x = position[0] + directions[direction][0]
    y = position[1] + directions[direction][1]
    position = (x, y)
    steps += 1

print("".join(letters))
print(steps)
