'''
    Advent of Code Day 8
    https://adventofcode.com/2020/day/8
'''

# input from website in raw format
data = []
with open('day8.input.txt', 'r') as f:
    data = f.read().splitlines()

# data = [
#     "nop +0",
#     "acc +1",
#     "jmp +4",
#     "acc +3",
#     "jmp -3",
#     "acc -99",
#     "acc +1",
#     "jmp -4",
#     "acc +6"
# ]

rules = {}
for index, line in enumerate(data):
    a, b = line.split(" ")
    b = int(b)
    collection = [a, b]
    rules[index+1] = collection


# Puzzle #1
def check_instructions(rules):
    accumulator = 0
    instruction = 1
    s = set()
    while True:
        if instruction in rules and instruction not in s:
            s.add(instruction)
            if rules[instruction][0] == "nop":
                instruction += 1
                continue
            elif rules[instruction][0] == "acc":
                accumulator += rules[instruction][1]
                instruction += 1
                continue
            elif rules[instruction][0] == "jmp":
                instruction += rules[instruction][1]
                continue
            else:
                print("Something has gone horribly wrong.")
                return
        else:
            if instruction > len(rules):
                return accumulator, True
            else:
                return accumulator, False

print(f"Answer for Puzzle #1: {check_instructions(rules)[0]}")


# Puzle #2
# we need copy.deepcopy to copy nested lists/dictionaries.... we have lists nested in our rules dictionary :-()
import copy

jmps = []
nops = []
for k,v in rules.items():
    if v[0] == "jmp":
        jmps.append(k)
        continue
    if v[0] == "nop":
        nops.append(k)
        continue

my_modified_jmp_rules = []
for i in range(0, len(jmps)):
    my_modified_jmp_rules.append(copy.deepcopy(rules))

my_modified_nop_rules = []
for i in range(0, len(nops)):
    my_modified_nop_rules.append(copy.deepcopy(rules))

for i in range(0, len(jmps)):
    my_modified_jmp_rules[i][jmps[i]][0] = "nop"

for i in range(0, len(nops)):
    my_modified_nop_rules[i][nops[i]][0] = "jmp"

lists_to_iterate_over = my_modified_jmp_rules + my_modified_nop_rules

# now check for the tuple that contains True
[ print(f"Answer for Puzzle #2: {check_instructions(x)[0]}") for x in lists_to_iterate_over if check_instructions(x)[1]]