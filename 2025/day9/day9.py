'''
    Advent of Code 2025
    https://adventofcode.com/2025/day/9
'''
from shapely.geometry import Polygon
from itertools import combinations

# input from website
sample_input = False
input = 'day9_sample.txt' if sample_input else 'day9.txt'
with open(input, 'r') as f:
    points = [list(map(int, line.split(",")))
              for line in f.read().splitlines()]


def area(p, q):
    return (abs(p[0]-q[0])+1)*(abs(p[1]-q[1])+1)

# p = (2, 5)
# q = (9, 7)
# assert (area(p, q) == 24)


# p = (7, 1)
# q = (11, 7)
# assert (area(p, q) == 35)


# p = (7, 3)
# q = (2, 3)
# assert (area(p, q) == 6)

# p = (2, 5)
# q = (11, 1)
# assert (area(p, q) == 50)

combs = list(combinations(points, 2))
print(max(area(c[0], c[1]) for c in combs))


def rect(p, q):
    return Polygon([
        (p[0], q[1]),
        (p[0], p[1]),
        (q[0], p[1]),
        (q[0], q[1])
    ])


poly = Polygon(points)
print(max(area(c[0], c[1])
      for c in combs if poly.contains(rect(c[0], c[1]))))
