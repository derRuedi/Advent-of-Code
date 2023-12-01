'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/1
'''

import re

# input from website
sample_input = False
input = 'day1_sample.txt' if sample_input else 'day1.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


# puzzle 1
def get_sums(data):
    my_sum = 0
    for line in data:
        nums = re.findall("\d", line)
        my_sum += int(nums[0] + nums[-1])
    return my_sum


# puzzle 2
def get_sums2(data):
    my_sum = 0
    nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for line in data:
        start_num = ""
        end_num = ""
        for i in range(len(line)):
            if line[i].isdigit():
                start_num = line[i]
                break
            for n in nums:
                if line[i:].startswith(n):
                    start_num = nums[n]
                    break
            if start_num:
                break

        for i in range(1, len(line)+1):
            if line[-i].isdigit():
                end_num = line[-i]
                break
            for n in nums:
                if line[-i:].startswith(n):
                    end_num = nums[n]
                    break
            if end_num:
                break
        my_sum += int(start_num + end_num)
    return my_sum


def get_sums2_better(data):
    my_sum = 0
    numbers = ["one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]
    for line in data:
        for i, n in enumerate(numbers):
            line = line.replace(n, n + str(i+1) + n)
        nums = re.findall("\d", line)
        my_sum += int(nums[0] + nums[-1])
    return my_sum


def get_sums2_regex(data):
    my_sum = 0
    r = '1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for line in data:
        nums = re.findall(rf'(?=({r}))', line)
        my_sum += int((nums[0] if nums[0].isdigit() else numbers[nums[0]]) +
                      (nums[-1] if nums[-1].isdigit() else numbers[nums[-1]]))
    return my_sum


print(get_sums(data))

print(get_sums2(data))
print(get_sums2_better(data))
print(get_sums2_regex(data))
