'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def preprocess_data(data):
    reindeer_descriptions = []
    for line in data:
        # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        # [0]   [1] [2] [3][4]  [5] [6][7]      [8] [9]  [10] [11] [12][13][14]

        # reindeer, _, _, speed, _, _, duration, _, _, _, _, _, _, rest, _ = \
        #     line.split(" ")

        description = line.split(" ")
        reindeer_descriptions.append(
            {
                "name": description[0],
                "speed": int(description[3]),
                "duration": int(description[6]),
                "rest": int(description[13]),
                "distance": 0,
                "points": 0
            }
        )
    return reindeer_descriptions


def puzzle1(data):
    reindeer_descriptions = preprocess_data(data)
    time = 2503
    for reindeer in reindeer_descriptions:
        run_rest_iterations = time // (reindeer["duration"] + reindeer["rest"])
        remainder = time % (reindeer["duration"] + reindeer["rest"])

        reindeer["distance"] = run_rest_iterations * \
            reindeer["speed"] * reindeer["duration"]

        if remainder > reindeer["duration"]:
            reindeer["distance"] += reindeer["speed"] * reindeer["duration"]
        elif remainder < reindeer["duration"]:
            reindeer["distance"] += reindeer["speed"] * remainder
        elif remainder == 0:
            pass
        else:
            print("something is not right")

    for reindeer in reindeer_descriptions:
        print(reindeer["distance"], reindeer["name"])

    print(max(reindeer_descriptions, key=lambda x: x["distance"])["distance"])


def puzzle2(data):
    reindeer_descriptions = preprocess_data(data)
    for time in range(1, 2503+1):
        # Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
        for reindeer in reindeer_descriptions:
            status = time % (reindeer["duration"] + reindeer["rest"])
            if status != 0 and status <= reindeer["duration"]:
                reindeer["distance"] += reindeer["speed"]

        leading_distance = max(reindeer_descriptions,
                               key=lambda x: x["distance"])["distance"]

        for reindeer in reindeer_descriptions:
            if reindeer["distance"] == leading_distance:
                reindeer["points"] += 1

    for reindeer in reindeer_descriptions:
        print(reindeer["distance"], reindeer["points"], reindeer["name"])

    print(max(reindeer_descriptions, key=lambda x: x["points"])["points"])


print("Puzzle 1 data:")
puzzle1(data)
print()
print("Puzzle 2 data:")
puzzle2(data)
