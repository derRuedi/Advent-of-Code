'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/7
'''

# input from website
from collections import defaultdict


sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

dir_stack = []
dir_sizes = defaultdict(int)

for line in data:
    match line.split():
        case ["$", "cd", ".."]:
            dir_stack.pop()
        case ["$", "cd", directory]:
            # print(f"{'  '*len(dir_stack)} - {directory} (dir)")
            dir_stack.append(directory)
        case ["$", "ls"]:
            pass
        case ["dir", directory]:
            pass
        case [size, filename]:
            # print(f"{'  '*len(dir_stack)} - {filename} (file, size={size})")
            dir_sizes[tuple(dir_stack)] += int(size)

            # file is in every directory, account for it
            parents = dir_stack[:-1]
            while parents:
                dir_sizes[tuple(parents)] += int(size)
                parents.pop()
        case _:
            print("something unhandled" * 100)

part1 = sum(d for d in dir_sizes.values() if d < 100000)
print(part1)

total_disk_size = 70_000_000
required_disk_size = 30_000_000
free_disk_size = total_disk_size - dir_sizes[tuple("/")]


part2 = min(d for d in dir_sizes.values()
            if free_disk_size + d > required_disk_size)
print(part2)
