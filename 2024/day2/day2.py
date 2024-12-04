'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/2
'''

# input from website
sample_input = False
input = 'day2_sample.txt' if sample_input else 'day2.txt'
with open(input, 'r') as f:
    # convert the input data to a list of ints
    data = [[int(n) for n in line.split()] for line in f.read().splitlines()]

MIN_LEVEL_DIFFERENCE = 1
MAX_LEVEL_DIFFERENCE = 3


def is_report_safe(report: list):
    differences = [j - i for i, j in zip(report, report[1:])]
    # are we within the boundaries for adjacent levels?
    if any(not (MIN_LEVEL_DIFFERENCE <= abs(difference) <= MAX_LEVEL_DIFFERENCE) for difference in differences):
        return False
    # are all increasing or all decreasing
    # (differences should not change sign)?
    if min(differences) < 0 and max(differences) > 0:
        return False
    return True


def is_report_safe_dampener(report: list):
    # create every sublist of original list
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_report_safe(new_report):
            return True
    return False


print(sum(is_report_safe(line) for line in data))
print(sum(is_report_safe_dampener(line) for line in data))
