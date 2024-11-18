'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/6
'''

# input from website
from icecream import ic
sample_input = True
input = 'day6_sample.txt' if sample_input else 'day6.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

data = [int(d) for d in data[0].split()]


def puzzle1(data):
    memory_bank = data
    known_states = [[*memory_bank]]
    cycles = 0
    while True:
        cycles += 1
        most_blocks_at_index = memory_bank.index(max(memory_bank))
        blocks = memory_bank[most_blocks_at_index]
        memory_bank[most_blocks_at_index] = 0
        counter = 1
        while blocks != 0:
            memory_bank[(most_blocks_at_index + counter) %
                        len(memory_bank)] += 1
            counter += 1
            blocks -= 1
        if memory_bank in known_states:
            break
        known_states.append([*memory_bank])
    return cycles


print(puzzle1(data))
# puzzle 2
# we just run it again - this works since we modified the variable "data" to a state from where the cycle begins anew
print(puzzle1(data))
