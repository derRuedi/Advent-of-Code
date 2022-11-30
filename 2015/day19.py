'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


medicine_molecule = data[-1]
replacements = [k.split(" => ") for k in data[0:-3]]
distinct_molecules = set()

print(medicine_molecule)

for r in replacements:
    for i in range(1, medicine_molecule.count(r[0]) + 1):
        distinct_molecules.add(helper.replace_nth(
            medicine_molecule, r[0], r[1], i))

print(len(distinct_molecules))
