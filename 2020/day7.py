'''
    Advent of Code Day 7
    https://adventofcode.com/2020/day/7
'''

import re

# input from website in raw format
data = []
with open('day7.input.txt', 'r') as f:
    data = f.read().splitlines()

# data = [
#     "light red bags contain 1 bright white bag, 2 muted yellow bags.",
#     "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
#     "bright white bags contain 1 shiny gold bag.",
#     "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
#     "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
#     "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
#     "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
#     "faded blue bags contain no other bags.",
#     "dotted black bags contain no other bags."
# ]

# shall be stored in a list
# my_puzzle = [re.sub(r"(\w*\s\w*)\sbags\scontain\s(.*)", r"\1:\2", x) for x in data]

bags = {}
for line in data:
    line = re.sub("(\sbags\.|\sbag\.|\sbags|\sbag)", "", line)
    line = re.sub("\scontain\s", ":", line)
    line = line.split(":")
    enclosing_bag = line[0]
    bags_inside = {}
    for bag_inside in line[1].split(", "):
        if bag_inside == "no other":
            continue
        nums = re.sub(r"(\d).*", r"\1", bag_inside)
        name = re.sub(r"\d\s(.*)", r"\1", bag_inside)
        bags_inside[name] = int(nums)
    bags[enclosing_bag] = bags_inside

# print(bags, end="\n\n")

# Puzzle #1
s = set()
def find_bag_containing_bag(name, rules):
    for bag_name,containing_bags in rules.items():
        # if bag_name is in the bags:
        if name in containing_bags:
            # print(f"bag_name:\t{bag_name} - containing_bags:\t{containing_bags}")
            find_bag_containing_bag(bag_name, rules)
            s.add(bag_name)

find_bag_containing_bag("shiny gold", bags)
print(f"The answer to puzzle #1 is: {len(s)}", end="\n\n")

# Puzzle #2
def find_num_bags_for_bag(name, rules):
    count = 0
    # print(f"called for {name}")
    for bag_name, bag_count in rules[name].items():
        # print(f"executing:\t    count += {bag_count} * (find_num_bags_for_bag({bag_name}, rules) + 1)")
        count += bag_count * (find_num_bags_for_bag(bag_name, rules) + 1)
    # print(count)
    return count

print(f"The answer to puzzle #2 is: {find_num_bags_for_bag('shiny gold', bags)}")
