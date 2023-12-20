'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/19
'''

# input from website
from functools import reduce
import re
from icecream import ic
sample_input = True
input = 'day19_sample.txt' if sample_input else 'day19.txt'
with open(input, 'r') as f:
    workflows, ratings = f.read().split("\n\n")
    workflows = {k: v.split(",") for w in workflows.splitlines()
                 for k, v in [w[:-1].split("{")]}
    ratings = [{k: int(v) for x in r[1:-1].split(",") for k, v in [x.split("=")]}
               for r in ratings.splitlines()]


def perform_workflow(part: dict, workflow: str):
    if workflow in ["A", "R"]:
        return workflow == "A"
    rules = workflows[workflow][:-1]
    final_rule = workflows[workflow][-1]

    for rule in rules:
        condition, result = rule.split(":")
        c, o, v = re.findall(r"(\w)([<>])(\d+)", condition)[0]
        if o == ">" and part[c] > int(v):
            return perform_workflow(part, result)
        if o == "<" and part[c] < int(v):
            return perform_workflow(part, result)

    return perform_workflow(part, final_rule)


print(sum([sum(part.values())
      for part in ratings if perform_workflow(part, "in")]))


def combinations(workflow, ranges):
    if workflow == "R":
        return 0

    if workflow == "A":
        return reduce(lambda a, b: a*b, [(e-s+1) for s, e in ranges.values()])

    rules = workflows[workflow][:-1]
    final_rule = workflows[workflow][-1]

    ic(workflow, reduce(lambda a, b: a*b,
       [(e-s+1) for s, e in ranges.values()]))

    value = 0
    for rule in rules:
        condition, result = rule.split(":")
        c, o, v = re.findall(r"(\w)([<>])(\d+)", condition)[0]
        v = int(v)
        start_c, end_c = ranges[c]

        if o == "<":
            yes = (start_c, v-1)
            no = (v, end_c)
        else:
            yes = (v+1, end_c)
            no = (start_c, v)

        if yes[0] <= yes[1]:
            new_ranges = dict(ranges)
            new_ranges[c] = yes
            value += combinations(result, new_ranges)
        if no[0] <= no[1]:
            ranges = dict(ranges)
            ranges[c] = no

    return value + combinations(final_rule, ranges)


ranges = {"x": (1, 4000), "m": (1, 4000),
          "a": (1, 4000), "s": (1, 4000)}
print(combinations("in", ranges))
