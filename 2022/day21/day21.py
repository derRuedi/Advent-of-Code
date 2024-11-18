'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/21
'''

import functools

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

monkeys = {}
for line in data:
    monkey = line.replace(":", "").split(" ")
    if len(monkey[1:]) == 1:
        monkeys[monkey[0]] = int(monkey[1])
    else:
        monkeys[monkey[0]] = monkey[1:]


# @functools.lru_cache(maxsize=None)
def find(monkey):
    if type(monkey) == int:
        return monkey
    if type(monkeys[monkey]) == int:
        return monkeys[monkey]
    if type(monkeys[monkey]) == list:
        match monkeys[monkey][1]:
            case "+":
                return find(monkeys[monkey][0]) + find(monkeys[monkey][2])
            case "-":
                return find(monkeys[monkey][0]) - find(monkeys[monkey][2])
            case "*":
                return find(monkeys[monkey][0]) * find(monkeys[monkey][2])
            case "/":
                return find(monkeys[monkey][0]) // find(monkeys[monkey][2])
            case "==":
                return find(monkeys[monkey][0]) == find(monkeys[monkey][2])


# part 1
print(find("root"))

# part 2
monkeys["root"][1] = "=="

i = 0
a, _, b = monkeys["root"]
while not find("root"):
    x = find(a)
    y = find(b)
    divisor = 100
    if abs(x - y) < 10000:
        i += 1
    else:
        if abs(x - y) > 0:
            i += abs(x - y) // divisor
        else:
            i -= abs(x - y) // divisor
    monkeys["humn"] = i
print(i)
