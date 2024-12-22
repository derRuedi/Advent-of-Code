'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/22
'''

import time
from operator import xor

# input from website
sample_input = False
input = 'day22_sample.txt' if sample_input else 'day22.txt'
with open(input, 'r') as f:
    data = list(map(int, f.read().splitlines()))


def calc_secret_number(num):
    result = xor(num * 64, num) % 16777216
    result = xor(result // 32, result) % 16777216
    result = xor(result * 2048, result) % 16777216
    return result


def sum_secret_numbers(data, iteration):
    result = 0
    for n in data:
        res = n
        for i in range(iteration):
            res = calc_secret_number(res)
        result += res
    return result


def ones_digit(num):
    return int(str(num)[-1])


def price_list_for_secret_number(num, length):
    price_list = [ones_digit(num)]
    for i in range(length):
        num = calc_secret_number(num)
        price_list.append(ones_digit(num))
    return price_list


def get_changes_in_price_list(price_list):
    return [b - a for a, b in zip(price_list, price_list[1:])]


def find_sublist_position(lst, sublist):
    n, m = len(lst), len(sublist)
    for i in range(n - m + 1):
        if lst[i:i + m] == sublist:
            return i  # Return the starting index
    return -1  # Return -1 if not found


def find_price_for_sequence(price_list, sequence, changes_in_price_l):
    pos = find_sublist_position(changes_in_price_l, sequence)
    if pos != -1:
        return price_list[pos + 4]
    return 0


print(f"puzzle 1: {sum_secret_numbers(data, 2000)}")


secret_num_data = {}

result = 0
all_cipl = []
for n in data:
    secret_num_data[n] = {
        "price_list": price_list_for_secret_number(n, 2000)
    }
    secret_num_data[n]["changes_in_price_list"] = get_changes_in_price_list(
        secret_num_data[n]["price_list"])

    secret_num_data[n]["sequence_price"] = {}
    all_sequences_in_n = [secret_num_data[n]["changes_in_price_list"][i:i + 4]
                          for i in range(len(secret_num_data[n]["changes_in_price_list"]) - 4 + 1)]

    for idx, seq_in_n in enumerate(all_sequences_in_n):
        seq_in_n = tuple(seq_in_n)
        if seq_in_n in secret_num_data[n]["sequence_price"]:
            continue
        secret_num_data[n]["sequence_price"][seq_in_n] = secret_num_data[n]["price_list"][idx+4]
    all_cipl += secret_num_data[n]["changes_in_price_list"]


all_unique_sequences = {tuple(sequence) for sequence in [all_cipl[i:i + 4]
                                                         for i in range(len(all_cipl) - 4 + 1)]}

all_prices = []

for idx, sequence in enumerate(all_unique_sequences):
    if idx % 1000 == 0:
        print(idx, "of", len(all_unique_sequences))
    result = []
    for n in data:
        if sequence in secret_num_data[n]["sequence_price"]:
            price = secret_num_data[n]["sequence_price"][sequence]
        else:
            price = 0
        result.append(price)
    all_prices.append(result)


print(max(sum(s) for s in all_prices))
