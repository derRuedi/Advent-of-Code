'''
    Advent of Code Day 10
    https://adventofcode.com/2020/day/10
'''

# input from website in raw format
#data = []
#with open('day10.input.txt', 'r') as f:
#    data = f.read().splitlines()

#data = [ int(x) for x in data ]

sample_data1 = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4
]

sample_data2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3
]

my_data = [
    138,
    3,
    108,
    64,
    92,
    112,
    44,
    53,
    27,
    20,
    23,
    77,
    119,
    62,
    121,
    11,
    2,
    37,
    148,
    34,
    83,
    24,
    10,
    79,
    96,
    98,
    127,
    7,
    115,
    19,
    16,
    78,
    133,
    61,
    82,
    91,
    145,
    39,
    33,
    13,
    97,
    55,
    141,
    1,
    134,
    40,
    71,
    54,
    103,
    101,
    26,
    47,
    90,
    72,
    126,
    124,
    110,
    131,
    58,
    12,
    142,
    105,
    63,
    75,
    50,
    95,
    69,
    25,
    68,
    144,
    86,
    132,
    89,
    128,
    135,
    65,
    125,
    76,
    116,
    32,
    18,
    6,
    38,
    109,
    111,
    30,
    70,
    143,
    104,
    102,
    120,
    31,
    41,
    17
]

data = my_data




data += [max(data)+3]
data.sort()

# Puzzle #1
current_joltage = 0
joltage_diff_1 = 0
joltage_diff_3 = 0

for i in range(0, len(data)):
    # print(f"index:\t{i}\t\tjoltage:\t{data[i]}")
    if data[i] - current_joltage == 1:
        joltage_diff_1 += 1
    elif data[i] - current_joltage == 3:
        joltage_diff_3 += 1
    else:
        # we added 0 as starting joltage at index 0, so we can ignore it
        if i == 0:
            continue
        # otherwise something has gone wrong
        print("Something wrong")
    current_joltage = data[i]

print(f"The answer to Puzzle #1")
print(f"\tnumber of 1-jolt differences: {joltage_diff_1}")
print(f"\tnumber of 3-jolt differences: {joltage_diff_3}")
print(f"\tnumber of 1-jolt differences multiplied by the number of 3-jolt differences: {joltage_diff_1 * joltage_diff_3}")
print()


# Puzzle #2

# works for small data sets... but is absolutely inefficient for larger input data
# def create_and_fill_arrangements(arrangement):
#     for i in range(0, len(arrangement)-2):
#         if arrangement[i+2] - arrangement[i] <= 3:
#             new_arrangement = arrangement[0:i+1] + arrangement[i+2:]
#             if new_arrangement not in arrangements:
#                 arrangements.append(new_arrangement)
#                 create_and_fill_arrangements(new_arrangement)

# create_and_fill_arrangements(data)
# print(f"The answer to Puzzle #2 is {len(arrangements)}")


# the most elegant solution I could find... and understand

def puzzle2(data):
    routes = {}
    routes[0] = 1
    for adapter in data:
        routes[adapter] = routes.get(adapter - 1, 0) + routes.get(adapter - 2, 0) + routes.get(adapter - 3, 0)
    print(f"Answer to puzzle #2: {routes[data[-1]]}")
    

print(data)
puzzle2(data)




