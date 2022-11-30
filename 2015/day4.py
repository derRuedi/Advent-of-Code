'''
    Advent of Code Day 3
    https://adventofcode.com/2015/day/3
'''

import hashlib

secret_key = "ckczppom"

i = 0
while True:
    hash_value = f"{secret_key}{i}"
    hash_result = hashlib.md5(hash_value.encode('utf-8')).hexdigest()
    if hash_result[0:5] == "00000":
        print(f"The answer to puzzle 1 is: {i}")
        break
    i += 1

i = 0
while True:
    hash_value = f"{secret_key}{i}"
    hash_result = hashlib.md5(hash_value.encode('utf-8')).hexdigest()
    if hash_result[0:6] == "000000":
        print(f"The answer to puzzle 2 is: {i}")
        break
    i += 1
