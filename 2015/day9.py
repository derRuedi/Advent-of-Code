'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper
from itertools import permutations

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


locations_and_distances = {}
unique_cities = set()
for d in data:
    a, b, distance = d.split(" ")[0::2]
    unique_cities.add(a)
    unique_cities.add(b)
    locations_and_distances[(a, b)] = int(distance)
    locations_and_distances[(b, a)] = int(distance)

routes = permutations(unique_cities, len(unique_cities))

distances_routes = []

for route in routes:
    sum = 0
    for i in range(len(route)-1):
        sum += locations_and_distances[(route[i], route[i+1])]
    distances_routes.append(sum)

print(f"The answer to puzzle 1 is: {min(distances_routes)}")
print(f"The answer to puzzle 1 is: {max(distances_routes)}")
