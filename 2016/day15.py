'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def calc_time_slot(data):
    time = 0
    discs = []

    for i, line in enumerate(data):
        no_of_positions, *_, cur_position = line[12:-1].split(" ")
        disc = [int(no_of_positions), int(cur_position)]
        # account for one second it takes for the ball to fall to each disk
        # it is easier to add one second to each new disk than to do it while calculating
        disc[1] = (disc[1] + i + 1) % disc[0]
        discs.append(disc)

    while True:
        for disc in discs:
            disc[1] = (disc[1] + 1) % disc[0]
        time += 1

        if sum(d[1] for d in discs) == 0:
            break
    print(time)


calc_time_slot(data)
data.append("Disc #7 has 11 positions; at time=0, it is at position 0.")
calc_time_slot(data)
