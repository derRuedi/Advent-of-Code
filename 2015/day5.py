'''
    Advent of Code Day 5
    https://adventofcode.com/2015/day/5
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def puzzle1(data):
    vowels = "aeiou"
    forbidden_strings = ["ab", "cd", "pq", "xy"]

    nice_strings = 0

    for line in data:
        forbidden_string_found = False
        double_letter_found = False
        no_of_vowels = 0

        for fs in forbidden_strings:
            if fs in line:
                forbidden_string_found = True
        if forbidden_string_found:
            continue
        for i, c in enumerate(line):
            if c in vowels:
                no_of_vowels += 1
            if not double_letter_found and i+1 < len(line) and line[i] == line[i+1]:
                double_letter_found = True

        if no_of_vowels >= 3 and double_letter_found and not forbidden_string_found:
            nice_strings += 1

    print(f"The answer to puzzle 1 is: {nice_strings}")


def puzzle2(data):
    nice_strings = 0
    for line in data:
        pair_of_letters_that_appear_twice_found = False
        letter_which_repeats_with_exactly_one_letter_between_them_found = False
        for i, c in enumerate(line):

            if not pair_of_letters_that_appear_twice_found and i+1 < len(line) and line.count(f"{line[i] + line[i+1]}") >= 2:
                pair_of_letters_that_appear_twice_found = True

            if not letter_which_repeats_with_exactly_one_letter_between_them_found and i+2 < len(line) and line[i] == line[i+2]:
                letter_which_repeats_with_exactly_one_letter_between_them_found = True

        if pair_of_letters_that_appear_twice_found and letter_which_repeats_with_exactly_one_letter_between_them_found:
            nice_strings += 1

    print(f"The answer to puzzle 2 is: {nice_strings}")


puzzle1(data)
puzzle2(data)
