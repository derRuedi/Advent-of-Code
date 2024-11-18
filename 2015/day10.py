'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

from hashlib import new
import pathlib
import helper

# input from website in raw format
data = "1113222113"


def calc_look_and_say(data, count):
    sequence = data
    for j in range(count):
        new_sequence = ""
        i = 0
        while i < len(sequence):
            number = sequence[i]
            count = 1
            while i+count < len(sequence) and sequence[i+count] == number:
                count += 1
            new_sequence += str(count) + str(number)
            i += count
        # print(f"{j} (sequence): {sequence}")
        # print(f"{j} (new_sequence): {new_sequence}")
        # print()
        sequence = new_sequence
    return len(new_sequence)


def puzzle1(data):
    print(f"The answer to puzzle 1 is: {calc_look_and_say(data, 40)}")


def puzzle2(data):
    print(f"The answer to puzzle 2 is: {calc_look_and_say(data, 50)}")


puzzle1(data)
puzzle2(data)
