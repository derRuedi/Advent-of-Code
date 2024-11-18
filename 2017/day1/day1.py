'''
Advent of Code Day 1
https://adventofcode.com/2017/day/1
'''

# input from website in raw format

with open('day1.input.txt', 'r') as f:
    data = f.read()

# sample input from website
# data = "123123"


def puzzle1(input_data):
    sum = 0
    for i in range(len(input_data)):
        # make sure list is circular
        # so the digit after the last digit is the first digit in the list
        # hence the '(i+1) % (len(input_data))' to compare the following
        if input_data[i] == input_data[(i+1) % (len(input_data))]:
            sum += int(input_data[i])
    print(sum)


def puzzle2(input_data):
    sum = 0
    for i in range(len(input_data)):
        # make sure list is circular
        # so the digit after the last digit is the first digit in the list
        # hence the '(i+1) % (len(input_data))' to compare the following
        if input_data[i] == input_data[(int(i+(len(input_data)/2))) % (len(input_data))]:
            sum += int(input_data[i])
    print(sum)


# puzzle1(data)
puzzle2(data)
