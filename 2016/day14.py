'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

from collections import defaultdict
import pathlib
import hashlib
import re

# input from website
input = "zpqevtbw"
keys = []
i = -1
triple = re.compile(r"(.)\1{2}")
calculated_hashes = defaultdict(str)

# # part 1 --> real    0m1.650s
# while len(keys) < 64:
#     i += 1
#     hash_result = hashlib.md5(f"{input}{i}".encode('utf-8')).hexdigest()
#     if triple.search(hash_result):
#         quintuple = re.compile(f"{triple.search(hash_result).group(1)}{{5}}")
#         for j in range(i+1, i+1001):
#             hash_result = hashlib.md5(
#                 f"{input}{j}".encode('utf-8')).hexdigest()
#             if quintuple.search(hash_result):
#                 keys.append(i)
#                 break
# print(keys[-1])

# part 1 - optimized --> real    0m0.733s
keys = []
while len(keys) < 64:
    i += 1
    if i in calculated_hashes:
        hash_result = calculated_hashes[i]
    else:
        hash_result = hashlib.md5(f"{input}{i}".encode('utf-8')).hexdigest()
        calculated_hashes[i] = hash_result
    if triple.search(hash_result):
        quintuple = re.compile(f"{triple.search(hash_result).group(1)}{{5}}")
        for j in range(i+1, i+1001):
            if j in calculated_hashes:
                hash_result = calculated_hashes[j]
            else:
                hash_result = hashlib.md5(
                    f"{input}{j}".encode('utf-8')).hexdigest()
                calculated_hashes[j] = hash_result
            if quintuple.search(hash_result):
                keys.append(i)
                break
print(keys[-1])

# part 2
keys = []
while len(keys) < 64:
    i += 1
    if i in calculated_hashes:
        hash_result = calculated_hashes[i]
    else:
        hash_result = hashlib.md5(f"{input}{i}".encode('utf-8')).hexdigest()
        for k in range(2016):
            hash_result = hashlib.md5(hash_result.encode('utf-8')).hexdigest()
        calculated_hashes[i] = hash_result
    if triple.search(hash_result):
        quintuple = re.compile(f"{triple.search(hash_result).group(1)}{{5}}")
        for j in range(i+1, i+1001):
            if j in calculated_hashes:
                hash_result = calculated_hashes[j]
            else:
                hash_result = hashlib.md5(
                    f"{input}{j}".encode('utf-8')).hexdigest()
                for k in range(2016):
                    hash_result = hashlib.md5(
                        hash_result.encode('utf-8')).hexdigest()
                calculated_hashes[j] = hash_result
            if quintuple.search(hash_result):
                keys.append(i)
                break
print(keys[-1])
print(len(calculated_hashes))
