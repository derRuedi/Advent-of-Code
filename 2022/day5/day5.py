'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/5
'''

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read()
    stack_config = data[:data.index("\n\n")].splitlines()
    moves = data[data.index("\n\n")+2:].splitlines()


# def initialize_stack(stack_config):
#     num_of_stacks = int(stack_config[-1].split()[-1])
#     stack_config = stack_config[:-1][::-1]
#     stacks = [[] for i in range(num_of_stacks)]

#     for line in stack_config:
#         for i in range(0, len(line), 4):
#             if line[i+1].isalpha():
#                 stacks[i//4].append(line[i+1])
#     return stacks


def initialize_stack(stack_config):
    stack_config = stack_config[:-1][::-1]
    return [[c for c in a if c != " "]
            for i, a in enumerate(zip(*stack_config)) if i % 4 == 1]


def move_cargo(stacks, cratemover=9000):
    for move in moves:
        amount, from_where, to_where = [int(a)
                                        for a in move.split() if a.isdigit()]
        cargo = stacks[from_where - 1][-amount:]
        stacks[from_where - 1] = stacks[from_where - 1][:-amount]
        if cratemover == 9001:
            stacks[to_where - 1] += cargo
        else:
            stacks[to_where - 1] += cargo[::-1]

    print("".join(l[-1] for l in stacks))


# puzzle 1
stacks = initialize_stack(stack_config)
move_cargo(stacks)

# puzzle 2
stacks = initialize_stack(stack_config)
move_cargo(stacks, cratemover=9001)
