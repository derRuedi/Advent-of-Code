'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib
from collections import defaultdict

# input from website in raw format
input = 3014387


# Josephus problem (https://www.youtube.com/watch?v=uCsD3ZGzMgE)
# easy solution:
# convert to binary, drop the MSB and append it as new LSB
num_in_binary_string = format(input, 'b')
MSB = num_in_binary_string[0]
solution = num_in_binary_string[1:] + MSB

# convert to decimal
print(int(solution, 2))
