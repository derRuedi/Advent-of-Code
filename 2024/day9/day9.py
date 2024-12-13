'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/9
'''

# input from website
import time
sample_input = False
input = 'day9_sample.txt' if sample_input else 'day9.txt'
with open(input, 'r') as f:
    disk_map = f.read()


start = time.time()


def split_list(lst, size):
    if len(lst) % 2 != 0:
        lst += "0"
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def compact_individual_blocks(individual_blocks):
    individual_blocks = individual_blocks[:]
    back = -1
    file_length = len(individual_blocks)
    free_space = str(individual_blocks).count(".")
    for idx, b in enumerate(individual_blocks):
        if idx == file_length - free_space:
            break
        if b != ".":
            continue
        while individual_blocks[back] == ".":
            back -= 1
        individual_blocks[idx] = individual_blocks[back]
        individual_blocks[back] = "."
    return [b for b in individual_blocks if b != "."]


splitted = split_list(disk_map, 2)
individual_blocks = []

for idx, data in enumerate(splitted):
    file_id = idx
    file_size, free_space = map(int, data)

    individual_blocks.extend([file_id]*file_size)
    individual_blocks.extend(["."]*free_space)


print(f"puzzle 1: {sum(
    idx*b for idx, b in enumerate(compact_individual_blocks(individual_blocks)))}")

part1 = time.time()
print(f"this took {part1 - start}")

# puzzle 2
# print(individual_blocks)
# print(" ".join(str(c) for c in individual_blocks))
file_positions = []
file_id = None
for idx in range(len(individual_blocks)-1, -1, -1):
    if file_id == individual_blocks[idx]:
        continue
    if individual_blocks[idx] == ".":
        continue
    file_id = individual_blocks[idx]
    length = 0
    while individual_blocks[idx] == individual_blocks[idx-length]:
        length += 1
    file_positions.append([idx-length+1, idx+1])
    # print(f"block {file_id} is from {idx+1} until {idx-length+1}")


# print(f"file positions\t{file_positions}")

def find_dot_lengths(individual_blocks):
    # find dots and their corresponding length in individual_blocks
    dot_lengths = []
    start = None
    for i, value in enumerate(individual_blocks):
        if value == '.':
            if start is None:  # Start of a new sequence
                start = i
        else:
            if start is not None:  # End of the current sequence
                dot_lengths.append((start, i - start))
                start = None

    # Handle the case where the list ends with '.'
    if start is not None:
        dot_lengths.append((start, len(individual_blocks) - start))
    return dot_lengths


for file in file_positions:
    # print("".join(str(c) for c in individual_blocks))
    dot_lengths = find_dot_lengths(individual_blocks)
    for dl in dot_lengths:
        file_length = file[1] - file[0]
        if dl[1] >= file_length and dl[0] < file[0]:
            difference = dl[1] - file_length

            # do the swap
            individual_blocks[dl[0]:dl[0]+dl[1]
                              ] = individual_blocks[file[0]:file[1]] + ["."] * difference
            individual_blocks[file[0]:file[1]] = ["."] * file_length
            break

# print(individual_blocks)
# print("".join(str(c) for c in individual_blocks))
print(f"puzzle 2: {sum(
    idx*b for idx, b in enumerate(individual_blocks) if b != ".")}")
end = time.time()
print(f"this took {end - part1}")
print(f"in total {end - start}")
