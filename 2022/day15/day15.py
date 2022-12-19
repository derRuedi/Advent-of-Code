'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/15
'''

from collections import defaultdict
import re
from termcolor import colored

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

pattern = re.compile(r"(-?\d+)")
data = [list(map(int, pattern.findall(line))) for line in data]

# sensors, beacons and distance
sensors_beacons_distance = []
for line in data:
    sensors_beacons_distance.append(
        {
            "sensor": (line[0], line[1]),
            "beacon": (line[2], line[3]),
            "distance": abs(line[0] - line[2]) + abs(line[1] - line[3])
        }
    )

check_y = 10 if sample_input else 2000000


value_set = set()
beacon_set = [sbd["beacon"] for sbd in sensors_beacons_distance]


for sbd in sensors_beacons_distance:
    # just to make it more readable
    distance = sbd["distance"]
    # cover the possible x-range, where the sensor could check (assume the maximum, i.e. as if S is on the same line as "check_y")
    for value in range(sbd["sensor"][0]-distance, sbd["sensor"][0]+distance+1):
        # now check if, from the given x-value, the sensor reaches the line we want to check, i.e. "check_y"
        # and if it is not a beacon
        if abs(sbd["sensor"][0] - value) + abs(sbd["sensor"][1] - check_y) <= distance and (value, check_y) not in beacon_set:
            value_set.update({value})

# part 1
print(len(value_set))

# -------------------------

# part 2
maximum_search_area = 4000000
# tuning frequency = multiplying the distress beacon's x coordinate by "maximum_search_area" and then adding its y coordinate
surrounding_area = defaultdict(int)

for sbd in sensors_beacons_distance:
    # we need to look around the area covered by the sensors
    distance = sbd["distance"] + 1
    for point in range(distance):
        point_upper_right = (sbd["sensor"][0] +
                             (distance - point),  sbd["sensor"][1] - point)
        point_upper_left = (sbd["sensor"][0] -
                            (distance - point),  sbd["sensor"][1] - point)
        point_bottom_right = (sbd["sensor"][0] +
                              (distance - point),  sbd["sensor"][1] + point)
        point_bottom_left = (sbd["sensor"][0] -
                             (distance - point),  sbd["sensor"][1] + point)

        if 0 <= point_upper_right[0] <= maximum_search_area and 0 <= point_upper_right[1] <= maximum_search_area:
            surrounding_area[point_upper_right] += 1
        if 0 <= point_upper_left[0] <= maximum_search_area and 0 <= point_upper_left[1] <= maximum_search_area:
            surrounding_area[point_upper_left] += 1
        if 0 <= point_bottom_right[0] <= maximum_search_area and 0 <= point_bottom_right[1] <= maximum_search_area:
            surrounding_area[point_bottom_right] += 1
        if 0 <= point_bottom_left[0] <= maximum_search_area and 0 <= point_bottom_left[1] <= maximum_search_area:
            surrounding_area[point_bottom_left] += 1

for p in sorted(surrounding_area, reverse=True, key=lambda x: surrounding_area[x]):
    point_in_sensor = False
    for sbd in sensors_beacons_distance:
        distance = sbd["distance"]
        if abs(sbd["sensor"][0] - p[0]) + abs(sbd["sensor"][1] - p[1]) <= distance:
            point_in_sensor = True
            break
    if not point_in_sensor:
        # tuning frequency = multiplying the distress beacon's x coordinate by "maximum_search_area" and then adding its y coordinate
        print(int(p[0] * maximum_search_area + p[1]))


# --------------------------------------------------------------------------------------------------------
# initial solution - works only for sample input --> need to find a solution, that does not need the array
# --------------------------------------------------------------------------------------------------------

# # sensors, beacons and distance
# sbd = []
# x_values = []
# y_values = []

# for line in data:
#     sbd.append(
#         {
#             "sensor": (line[0], line[1]),
#             "beacon": (line[2], line[3]),
#             "distance": abs(line[0] - line[2]) + abs(line[1] - line[3])
#         }
#     )
#     x_values.append(sbd[-1]["sensor"][0] - sbd[-1]["distance"])
#     x_values.append(sbd[-1]["sensor"][0] + sbd[-1]["distance"])
#     y_values.append(sbd[-1]["sensor"][1] - sbd[-1]["distance"])
#     y_values.append(sbd[-1]["sensor"][1] + sbd[-1]["distance"])

# min_x = min(x_values)
# max_x = max(x_values)

# min_y = min(y_values)
# max_y = max(y_values)

# x_offset = abs(min_x)
# y_offset = abs(min_y)

# print("min_x", min_x)
# print("max_x", max_x)

# print("min_y", min_y)
# print("max_y", max_y)

# # initialize matrix
# matrix = [["." for x in range(max_x - min_x + 1)]
#           for y in range(max_y - min_y + 1)]


# def print_matrix(matrix):
#     print()
#     # header row
#     spacer = " "
#     print(
#         f"\t{spacer.join([' ' if l % 5 != 0 else str(l)[-1] for l in range(min_x, max_x)])}")

#     # actual matrix
#     for i, line in enumerate(matrix):
#         print(
#             f"{i+min_y}\t{spacer.join([l if l in ['.', '#'] else colored(l, 'red', attrs=['bold'])for l in line])}")
#     print()


# for line in sbd:
#     print(line)
#     matrix[line["sensor"][1] + y_offset][line["sensor"][0] + x_offset] = "S"
#     matrix[line["beacon"][1] + y_offset][line["beacon"][0] + x_offset] = "B"

#     #line = sbd[6]

#     distance = line["distance"]
#     for y in range(-distance, distance+1):
#         for x in range(-distance, distance+1):
#             if abs(x)+abs(y) <= distance and matrix[y+y_offset+line["sensor"][1]][x+x_offset+line["sensor"][0]] == ".":
#                 matrix[y+y_offset+line["sensor"][1]][x +
#                                                      x_offset+line["sensor"][0]] = "#"


# print_matrix(matrix)

# print(matrix[2000000+y_offset].count("#"))
