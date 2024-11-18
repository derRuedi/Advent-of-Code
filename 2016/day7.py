'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib
import re

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()

num = 0
for ipaddr in data:
    sequences = re.split(r"\[[a-z]+\]", ipaddr)
    hypernet_sequences = re.findall(r"\[([a-z]+)\]", ipaddr)
    sequences_reg = re.search(r"([a-z])(?!\1)([a-z])\2\1", " ".join(sequences))
    hypernet_sequences_reg = re.search(
        r"([a-z])(?!\1)([a-z])\2\1", " ".join(hypernet_sequences))
    # print(sequences_reg)
    # print(hypernet_sequences_reg)
    if sequences_reg != None and hypernet_sequences_reg == None:
        num += 1

print(num)


num = 0
for ipaddr in data:
    sequences = re.split(r"\[[a-z]+\]", ipaddr)
    hypernet_sequences = re.findall(r"\[([a-z]+)\]", ipaddr)

    # use a capturing group inside a lookahead (the '(?=' part), to catch overlapping matches
    # https://stackoverflow.com/questions/5616822/how-to-use-regex-to-find-all-overlapping-matches
    sequences_reg = re.findall(
        r"(?=([a-z])(?!\1)([a-z])\1)", " ".join(sequences))
    if sequences_reg:
        BAB = []
        for seq in sequences_reg:
            BAB.append(
                re.search(f"{seq[1]}{seq[0]}{seq[1]}", " ".join(hypernet_sequences)))
        if any(BAB):
            num += 1

print(num)
