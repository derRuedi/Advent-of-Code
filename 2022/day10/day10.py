'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/10
'''

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = [l.split() for l in f.read().splitlines()]


line = 0
tock = False
cycle = 1
register = {"x": 1}
signal_strength = []
crt = [" " for _ in range(240)]

while line <= len(data)-1:
    # part 2
    sprite = [register["x"]+i for i in range(-1, 2)]
    if (cycle-1) % 40 in sprite:
        crt[cycle-1] = "#"

    # part 1
    instruction = data[line]
    match instruction[0]:
        case "noop":
            cycle += 1
            line += 1
        case "addx":
            if tock:
                register["x"] += int(instruction[1])
                tock = False
                line += 1
            else:
                tock = True
            cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength.append(register["x"] * cycle)

# print part 1
print(sum(signal_strength), end="\n\n")

# print part 2
for i in range(1, 240+1):
    if i % 40 == 0:
        print(crt[i-1])
    else:
        print(crt[i-1], end="")
