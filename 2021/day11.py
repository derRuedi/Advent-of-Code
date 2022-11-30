'''
    Advent of Code Day 11
    https://adventofcode.com/2021/day/11
'''

data = []
with open("day11.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526"
]


def process_input_data(data):
    new_data = []
    for line in data:
        new_data.append([int(i) for i in line])
    return new_data


def print_map(data, with_tabs=False):
    for line in data:
        for num in line:
            print(num, end="\t" if with_tabs else "")
        print()
    print()


def process_step(data):
    # create points that are affected by flashing octopus
    neighbor = []
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if x == 0 and y == 0:
                continue
            neighbor.append((x, y))
    max_x = len(data[0])
    max_y = len(data)

    # increase energy level of every octopus by 1
    # keep track of which octopus will flash during iteration
    # for now only because the energy level has increased during the step
    octopus_will_flash = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            data[y][x] += 1
            # octopus will flash
            if data[y][x] > 9:
                octopus_will_flash.add((x, y))
    # now we have all the octopuses that will flash naturally

    octopuses_flashed = set()

    while True:
        # let them flash!
        for octopus in octopus_will_flash:
            for n in neighbor:
                x = octopus[0] + n[0]
                y = octopus[1] + n[1]
                # disregard edge cases
                if x < 0 or x >= max_x or y < 0 or y >= max_y:
                    continue
                # increase surrounding octopus
                data[y][x] += 1
            octopuses_flashed.add(octopus)

        # print(f"octopuses_flashed : {len(octopuses_flashed)} : {octopuses_flashed}")

        octopus_will_flash = set()
        for y in range(len(data)):
            for x in range(len(data[0])):
                # octopus will flash
                if data[y][x] > 9 and ((x, y) not in octopuses_flashed):
                    octopus_will_flash.add((x, y))

        # if there are no additional octopuses that will flash, break
        if not octopus_will_flash:
            break

    # reset octopuses that flashed
    for octopus in octopuses_flashed:
        x = octopus[0]
        y = octopus[1]
        data[y][x] = 0

    return len(octopuses_flashed)


def puzzle1(data):
    new_data = process_input_data(data)
    sum = 0
    for i in range(1, 100+1):
        sum += process_step(new_data)
    return sum


def puzzle2(data):
    new_data = process_input_data(data)
    result = 0
    step = 0
    while result != 100 or step == 10000:
        # step == 10000 is just precautionary
        result = process_step(new_data)
        step += 1
    return step


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
