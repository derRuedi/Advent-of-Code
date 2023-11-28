'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/7
'''

from collections import defaultdict
from icecream import ic

# input from website
sample_input = True
input = 'day7_sample.txt' if sample_input else 'day7.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


def prepare_data(data):
    new_data = defaultdict(dict)
    for line in data:
        split = line.split()
        if len(split) == 2:
            new_data[split[0]]["weight"] = int(split[1][1:-1])

        else:
            new_data[split[0]]["weight"] = int(split[1][1:-1])
            new_data[split[0]]["children"] = [
                s.replace(",", "") for s in split[3:]]

            for child in new_data[split[0]]["children"]:
                new_data[child]["parent"] = split[0]
    return new_data


def get_weight(data, node):
    if "children" not in data[node].keys():
        return data[node]["weight"]
    else:
        ic(node)
        data[node]["children_weight"] = [get_weight(
            data, child) for child in data[node]["children"]]

        ic(data[node]["children_weight"])

        return sum(data[node]["children_weight"])

    # for k, v in data.items():
    #     if 'children' not in v.keys():
    #         continue
    #     else:
    #         if 'parent' not in v.keys():
    #             continue

    #         if "children_weight" in new_data[v["parent"]].keys():
    #             new_data[v["parent"]]["children_weight"] += v["weight"]
    #         else:
    #             new_data[v["parent"]]["children_weight"] = v["weight"]


new_data = prepare_data(data)


bottom_program = [
    k for k, v in new_data.items() if 'parent' not in v.keys()][0]
print(
    f"Puzzle #1: The name of the bottom program is: '{bottom_program}'")

ic(new_data)

get_weight(new_data, bottom_program)

print("-"*100)

ic(new_data)
