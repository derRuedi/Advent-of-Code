'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/12
'''

from collections import defaultdict
from queue import PriorityQueue
import string

from termcolor import colored

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def process_input_data(data):
    matrix = [[string.ascii_lowercase.index(a) if a in string.ascii_lowercase else a for a in c]
              for c in data]

    contenders = []

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "S":
                start = (x, y)
                matrix[y][x] = string.ascii_lowercase.index("a")
            elif matrix[y][x] == "E":
                end = (x, y)
                matrix[y][x] = string.ascii_lowercase.index("z")
            elif matrix[y][x] == 0:
                contenders.append((x, y))
            else:
                continue
    return start, end, matrix, contenders


def create_costs_and_graph(matrix):
    graph = defaultdict(list)
    costs = {}

    neighbors = [
        (+1, 0),
        (0, +1),
        (-1, 0),
        (0, -1)
    ]

    max_x = len(matrix[0])
    max_y = len(matrix)

    for y in range(max_y):
        for x in range(max_x):
            for neighbor in neighbors:
                p_x = x + neighbor[0]
                p_y = y + neighbor[1]
                if p_x < 0 or p_x >= max_x or p_y < 0 or p_y >= max_y:
                    continue
                if matrix[y][x] >= matrix[p_y][p_x] - 1:
                    graph[(x, y)].append((p_x, p_y))
                    costs[(x, y), (p_x, p_y)] = 1
    return costs, graph


def dijkstra(graph, costs, start, end):
    # initialize
    costs_all_points = {k: float('inf') for k in graph.keys()}
    costs_all_points[end] = float('inf')
    costs_all_points[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))

    processed = set()

    while not queue.empty():
        node = queue.get()[1]
        processed.add(node)
        for point in graph[node]:
            if costs_all_points[node] + costs[node, point] < costs_all_points[point]:
                costs_all_points[point] = costs_all_points[node] + \
                    costs[node, point]
                if point not in processed:
                    queue.put((costs_all_points[point], point))

    return costs_all_points[end]


def print_matrix(matrix, path=[]):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if (x, y) in path:
                print(colored(matrix[y][x], "red", attrs=["bold"]), end="\t")
            else:
                print(matrix[y][x], end="\t")
        print()
    print()


start, end, matrix, contenders = process_input_data(data)
costs, graph = create_costs_and_graph(matrix)

# part 1
print(dijkstra(graph, costs, start, end))

# part 2
routes = [dijkstra(graph, costs, contender, end) for contender in contenders]
print(min(routes))
