'''
    Advent of Code Day 15
    https://adventofcode.com/2021/day/15
'''
from termcolor import colored
from collections import defaultdict
from queue import PriorityQueue

data = []
with open("day15.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581"
]


def process_input_data(data):
    new_data = []
    for line in data:
        new_data.append([int(i) for i in line])
    return new_data


def print_matrix(matrix, path=[]):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if (x, y) in path:
                print(colored(matrix[y][x], "red", attrs=["bold"]), end="")
            else:
                print(matrix[y][x], end="")
        print()
    print()


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
                graph[(x, y)].append((p_x, p_y))
                costs[(x, y), (p_x, p_y)] = matrix[p_y][p_x]

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


def multiply_cavern(matrix):
    matrix = process_input_data(matrix)
    new_matrix = []
    new_matrix2 = []
    for line in matrix:
        new_line = line + [(i+1) % 9 if (i+1 != 9) else 9 for i in line] + [(i+2) % 9 if (i+2 != 9) else 9 for i in line] + \
            [(i+3) % 9 if (i+3 != 9) else 9 for i in line] + \
            [(i+4) % 9 if (i+4 != 9) else 9 for i in line]
        new_matrix.append(new_line)
        new_matrix2.append(new_line)

    for i in range(1, 5):
        for line in new_matrix2:
            new_matrix.append(
                [(j+i) % 9 if (j+i != 9) else 9 for j in line]
            )

    return new_matrix


def calculate_minimum_path(matrix):
    costs, graph = create_costs_and_graph(matrix)
    start = (0, 0)
    end = (len(matrix[0])-1, len(matrix)-1)
    return dijkstra(graph, costs, start, end)


def puzzle1(data):
    matrix = process_input_data(data)
    return calculate_minimum_path(matrix)


def puzzle2(data):
    matrix = process_input_data(data)
    five_x_five_matrix = multiply_cavern(matrix)
    return calculate_minimum_path(five_x_five_matrix)

    cavern = process_input_data(data)
    costs, graph = create_costs_and_graph(new_cavern)
    start = (0, 0)
    end = (len(new_cavern[0])-1, len(new_cavern)-1)
    return dijkstra(graph, costs, start, end)


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
