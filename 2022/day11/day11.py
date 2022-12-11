'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/11
'''

from copy import deepcopy
import input_manual
import sample_input_manual

from functools import reduce
from math import gcd


def calc_monkey_business(monkeys, rounds, worry_level_workaround=False):
    if worry_level_workaround:
        # to keep worry level small, make use of the fact that
        # (a mod km) mod m = a mod m
        # to calculate k, we need the divisors of all monkeys
        divisors = [m["test"] for m in monkeys]
        # k is the product of all divisors
        k = reduce(lambda x, y: x*y, divisors)
    for round in range(rounds):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                old = monkey["items"].pop(0)
                new = eval(monkey["operation"])

                if worry_level_workaround:
                    # (a mod km) mod m = a mod m
                    new = new % k
                else:
                    new = new // 3

                if new % monkey["test"] == 0:
                    monkeys[monkey["test_true"]]["items"].append(new)
                else:
                    monkeys[monkey["test_false"]]["items"].append(new)
                monkey["inspected_items"] += 1

    inspected_items_ranked = [m["inspected_items"] for m in monkeys]
    inspected_items_ranked.sort()
    print(inspected_items_ranked[-1] * inspected_items_ranked[-2])


# input from website
sample_input = False
m = deepcopy(sample_input_manual.monkeys) if sample_input else deepcopy(
    input_manual.monkeys)
calc_monkey_business(m, 20)

m = deepcopy(sample_input_manual.monkeys) if sample_input else deepcopy(
    input_manual.monkeys)
calc_monkey_business(m, 10000, True)
