'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/12
'''
# input from website
from functools import cache
import re
sample_input = False
input = 'day12_sample.txt' if sample_input else 'day12.txt'
with open(input, 'r') as f:
    condition_records = [cr.split() for cr in f.read().splitlines()]

arrangements = []
for record, info in condition_records:
    info = list(map(int, info.split(",")))
    no_of_question_marks = record.count("?")
    no_of_valid_octothorpes = sum(info)
    max_i = int(str("1" * no_of_question_marks), 2)
    regex = r"".join([f"#{{{n}}}\.+" for n in info])[:-3]

    possible_combinations = [
        list(format(i, f'0{no_of_question_marks}b')) for i in range(max_i + 1) if format(i, f'0{no_of_question_marks}b').count("1") == no_of_valid_octothorpes]

    m = 0
    for c in possible_combinations:
        record_to_test = "".join([("." if c.pop(0) == "1" else "#")
                                  if b == "?" else b for b in record])
        if re.search(regex, record_to_test):
            m += 1

    arrangements.append(m)

print(sum(arrangements))


@cache
def my_recursion(record, info):
    # exits
    if len(record) == 0 and len(info) == 0:
        return 1

    if len(record) == 0 and len(info) > 0:
        return 0

    if len(info) == 0:
        return 1 if record.count("#") == 0 else 0

    # recursion
    amount = 0

    if record[0] == ".":  # discard the . and keep on checking
        amount += my_recursion(record[1:], info)

    if record[0] == "?":  # treat the ? as dot and keep on checking
        amount += my_recursion(record[1:], info)

    if record[0] in "?#":  # treating the ? as # is the same as if it actually is a #
        # is the record string long enough for the group against which we check
        if info[0] <= len(record):
            if "." not in record[: info[0]]:  # if there is a dot, it does not match

                # we are at the end, do we have more groups? --> exits
                if info[0] == len(record):
                    amount += my_recursion(record[info[0] + 1:], info[1:])
                elif record[info[0]] != "#":  # we can't have more # than specified in the group
                    amount += my_recursion(record[info[0] + 1:], info[1:])
    return amount


arrangements = []
no_of_copies = 5

for record, info in condition_records:
    record = '?'.join([record] * no_of_copies)
    # @cache can only be used with hashable data types
    info = tuple([int(n) for n in info.split(',')] * no_of_copies)

    arrangements.append(my_recursion(record, info))
print(sum(arrangements))
