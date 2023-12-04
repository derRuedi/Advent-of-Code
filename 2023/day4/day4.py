'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/4
'''

# input from website
from collections import defaultdict
from functools import reduce


sample_input = False
input = 'day4_sample.txt' if sample_input else 'day4.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

all_cards = []

for line in data:
    card, card_data = line.split(":")
    card_number = card.split()[1]
    winning_numbers, card_numbers = card_data.split("|")
    winning_numbers = [int(wn) for wn in winning_numbers.split()]
    card_numbers = [int(cn) for cn in card_numbers.split()]
    no_of_winners = sum(1 for cn in card_numbers if cn in winning_numbers)
    points = 2 ** (no_of_winners - 1) if no_of_winners > 0 else 0
    all_cards.append({
        "card_number": card_number,
        "amount": 1,
        "matching_numbers": no_of_winners,
        "points_won": points
    })

print(sum([c["points_won"] for c in all_cards]))

for pos, card in enumerate(all_cards):
    for i in range(min(card["matching_numbers"], len(all_cards)-1-pos)):
        all_cards[pos+i+1]["amount"] += card["amount"]

print(sum([c["amount"] for c in all_cards]))
