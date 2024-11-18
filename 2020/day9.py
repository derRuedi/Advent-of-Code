'''
    Advent of Code Day 9
    https://adventofcode.com/2020/day/9
'''

# input from website in raw format
data = []
with open('day9.input.txt', 'r') as f:
    data = f.read().splitlines()

data = [ int(x) for x in data ]
preamble = 25

# data = [
#     35,
#     20,
#     15,
#     25,
#     47,
#     40,
#     62,
#     55,
#     65,
#     95,
#     102,
#     117,
#     150,
#     182,
#     127,
#     219,
#     299,
#     277,
#     309,
#     576
# ]
# preamble = 5

# Puzzle #1
def is_sum_of_previous_nums(num, data):
    for i in range(0, len(data)-1):
        for j in range(i+1, len(data)):
            if i == j:
                continue
            if (data[i] + data[j] == num):
                # print(f"{data[i]} + {data[j]} == {num}  \t\t    data[{i}] + data[{j}] == {num}")
                return True
    return False


iterator = 0
invalid_number = 0
while iterator + preamble < len(data):
    num = data[iterator + preamble]

    subdata = data[iterator:iterator + preamble]
    if not is_sum_of_previous_nums(num, subdata):
        print(f"The answer to Puzzle #1 is: {num}")
        invalid_number = num
    iterator += 1


# Puzzle #2
my_sum = 0
iterator = 0
restart = True

while restart:
    for i in range(iterator, len(data)):
        my_sum += data[i]
        if my_sum > invalid_number:
            iterator += 1
            my_sum = 0
            break
        elif my_sum == invalid_number:
            # print(f"We have a result: from {iterator} until {i}.")
            # print(f"\t  {data[iterator:i+1]} = {sum(data[iterator:i+1])}")
            # print(f"\t  {min(data[iterator:i+1])} + {max(data[iterator:i+1])} = {min(data[iterator:i+1]) + max(data[iterator:i+1])}")
            print(f"The answer to Puzzle #2 is: {min(data[iterator:i+1]) + max(data[iterator:i+1])}")
            restart = False
            break
        