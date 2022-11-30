'''
    Advent of Code Day 12
    https://adventofcode.com/2021/day/12
'''

data = []
with open("day12.input.txt", "r") as f:
    data = [line.split("-") for line in f.read().splitlines()]

sample_data1 = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]

sample_data2 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc"
]

sample_data3 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW"
]

sample_data = [line.split("-") for line in sample_data1]


def build_graph(edges):
    graph = {}

    for a, b in edges:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = list()
            graph[a].append(b)
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = list()
            graph[b].append(a)

    return graph


def find_all_paths(graph, start, end):
    all_paths = [[start]]
    for path in all_paths:
        node = path[-1]
        if node == end:
            continue
        small_caves_in_path = [cave for cave in path if cave.islower()]
        for neighbor in graph[node]:
            if neighbor in small_caves_in_path:
                continue
            new_path = list(path)
            new_path.append(neighbor)
            all_paths.append(new_path)

    # print("Solutions:")
    # for path in all_paths:
    #     if (path[0] == start and path[-1] == end):
    #         print(path)

    return [path for path in all_paths if (path[0] == start and path[-1] == end)]


def find_all_paths_small_caves_twice(graph, start, end):
    all_paths = [[start]]
    i = 0
    for idx, path in enumerate(all_paths):
        node = path[-1]
        if node == end:
            continue

        for neighbor in graph[node]:
            if neighbor == start:
                continue

            new_path = list(path)
            new_path.append(neighbor)
            if is_path_valid(new_path):
                all_paths.append(new_path)

    # print("Solutions:")
    # for path in all_paths:
    #     if (path[0] == start and path[-1] == end):
    #         print(path)

    return [path for path in all_paths if (path[0] == start and path[-1] == end)]


def is_path_valid(path):
    # a path is invalid if a small cave has been visited more than twice
    # or if more than one small cave is visited twice

    # in other words:
    # big caves can be visited any number of times,
    # a single small cave can be visited at most twice,
    # and the remaining small caves can be visited at most once.
    small_caves_in_path = [cave for cave in path if cave.islower()]
    unique_small_caves = set(small_caves_in_path)

    a = []
    for small_cave in unique_small_caves:
        a.append(small_caves_in_path.count(small_cave))
    a.sort()
    b = [i for i in a if i > 1]

    if len(b) > 1 or a[-1] > 2:
        return False
    else:
        return True


def puzzle1(data):
    graph = build_graph(data)
    paths = find_all_paths(graph, "start", "end")
    return len(paths)


def puzzle2(data):
    graph = build_graph(data)
    paths = find_all_paths_small_caves_twice(graph, "start", "end")
    return len(paths)


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
