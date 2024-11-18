'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/8
'''

from functools import reduce

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = [[int(c) for c in a] for a in f.read().splitlines()]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def initialize_trees(data):
    trees = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            trees[(x, y)] = {
                "height": data[y][x],
                "visible": True if x == 0 or y == 0 or x == len(data)-1 or y == len(data[0])-1 else False,
                "scenic_score": [0]
            }
    return trees


def print_trees(trees, values=["height"], highlight=None):
    for y in range(len(data)):
        for x in range(len(data[0])):
            for value in values:
                if (x, y) == highlight:
                    print(bcolors.OKGREEN + str(trees[(x, y)]
                                                [value]) + bcolors.ENDC, end=" ")
                else:
                    print(trees[(x, y)][value], end=" ")
            print("", end="\t")
        print()


trees = initialize_trees(data)

max_x = len(data[0])
max_y = len(data)
for y in range(1, max_y-1):
    for x in range(1, max_x-1):
        # check to the left
        for check_x in range(1, x+1):
            if trees[(x-check_x, y)]["height"] >= trees[(x, y)]["height"]:
                break
        else:
            trees[(x, y)]["visible"] = True

        # check to the right
        for check_x in range(1, max_x - x):
            if trees[(x+check_x, y)]["height"] >= trees[(x, y)]["height"]:
                break
        else:
            trees[(x, y)]["visible"] = True

        # check up
        for check_y in range(1, y+1):
            if trees[(x, y-check_y)]["height"] >= trees[(x, y)]["height"]:
                break
        else:
            trees[(x, y)]["visible"] = True

        # check down
        for check_y in range(1, max_y - y):
            if trees[(x, y+check_y)]["height"] >= trees[(x, y)]["height"]:
                break
        else:
            trees[(x, y)]["visible"] = True


print(sum(1 for t in trees.values() if t["visible"]))


# scenic score
# DISCLAIMER: apparently there is no need to adjust "height"
# elves can see trees as long as there is no tree larger than their own in front of them
for y in range(1, max_y-1):
    for x in range(1, max_x-1):
        scenic_score = []

        # check to the left
        height = 0
        score = 0
        for check_x in range(1, x+1):
            if trees[(x-check_x, y)]["height"] >= trees[(x, y)]["height"]:
                score += 1
                break
            elif trees[(x-check_x, y)]["height"] >= height:
                score += 1
                # height = trees[(x-check_x, y)]["height"]
            else:
                continue
        scenic_score.append(score)

        # check to the right
        height = 0
        score = 0
        for check_x in range(1, max_x - x):
            if trees[(x+check_x, y)]["height"] >= trees[(x, y)]["height"]:
                score += 1
                break
            elif trees[(x+check_x, y)]["height"] >= height:
                score += 1
                # height = trees[(x+check_x, y)]["height"]
            else:
                continue
        scenic_score.append(score)

        # check up
        height = 0
        score = 0
        for check_y in range(1, y+1):
            if trees[(x, y-check_y)]["height"] >= trees[(x, y)]["height"]:
                score += 1
                break
            elif trees[(x, y-check_y)]["height"] >= height:
                score += 1
                # height = trees[(x, y-check_y)]["height"]
            else:
                continue
        scenic_score.append(score)

        # check down
        height = 0
        score = 0
        for check_y in range(1, max_y - y):
            if trees[(x, y+check_y)]["height"] >= trees[(x, y)]["height"]:
                score += 1
                break
            elif trees[(x, y+check_y)]["height"] >= height:
                score += 1
                # height = trees[(x, y+check_y)]["height"]
            else:
                continue
        scenic_score.append(score)

        # reduce(lambda x, y: x*y, scenic_score)
        trees[(x, y)]["scenic_score"] = scenic_score

print(max(reduce(lambda x, y: x*y, t["scenic_score"]) for t in trees.values()))
