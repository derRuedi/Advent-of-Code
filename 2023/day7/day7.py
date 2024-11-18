'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/7
'''
from collections import Counter

# input from website
sample_input = False
input = 'day7_sample.txt' if sample_input else 'day7.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


all_hands = [{"hand": hand, "bid": int(bid)}
             for line in data for hand, bid in [line.split()]]


def camel_hand_value(hand, joker=False):
    c = Counter(hand["hand"])
    js = c["J"]
    if not joker or js == 0:
        match sorted(c.values()):
            case [1, 1, 1, 1, 1]:  # high card
                hand["value"] = 0
            case [1, 1, 1, 2]:  # one pair
                hand["value"] = 1e10
            case [1, 2, 2]:  # two pair
                hand["value"] = 1e11
            case [1, 1, 3]:  # three of a kind
                hand["value"] = 1e12
            case [2, 3]:  # full house
                hand["value"] = 1e13
            case [1, 4]:  # four of a kind
                hand["value"] = 1e14
            case [5]:  # five of a kind
                hand["value"] = 1e15
            case _:
                pass
    else:
        del c["J"]
        match sorted(c.values()):
            # 1 joker
            case [1, 1, 1, 1]:  # one pair (high card + 1 joker)
                hand["value"] = 1e10
            case [1, 1, 2]:  # three of a kind (one pair + 1 joker)
                hand["value"] = 1e12
            case [2, 2]:  # full house (two pair + 1 joker)
                hand["value"] = 1e13
            case [1, 3]:  # four of a kind (three of a kind + 1 joker)
                hand["value"] = 1e14
            case [4]:  # five of a kind (four of a kind + 1 joker)
                hand["value"] = 1e15

            # 2 joker
            case [1, 1, 1]:  # three of a kind (3 card + 2 joker)
                hand["value"] = 1e12
            case [1, 2]:  # four of a kind (1 pair + 2 joker)
                hand["value"] = 1e14
            case [3]:  # five of a kind (1 three of a kind + 2 joker)
                hand["value"] = 1e15

            # 3 joker
            case [1, 1]:  # four of a kind (2 cards + 3 joker)
                hand["value"] = 1e14
            case [2]:  # five of a kind (1 pair + 3 joker)
                hand["value"] = 1e15

            # 4 joker
            case [1]:  # five of a kind (1 card + 4 joker)
                hand["value"] = 1e15

            # 5 joker
            case []:  # five of a kind (5 joker)
                hand["value"] = 1e15

            case _:
                print(
                    f"did you think of ({js} jokers):\t {hand['hand'].upper()} -\t {c.values()}")

    card_order_values = [1, 1e2, 1e4, 1e6, 1e8]  # for high card and ties
    card_order = '23456789TJQKA' if not joker else 'J23456789TQKA'
    card_values = {card: value+1 for value, card in enumerate(card_order)}
    for x, c in enumerate(hand["hand"][::-1]):
        hand["value"] += card_order_values[x] * card_values[c]


def calculate_total_winnings(hands, joker=False):
    for hand in hands:
        camel_hand_value(hand, joker)

    total_winnings = 0
    for rank, hand in enumerate(sorted(all_hands, key=lambda hand: hand["value"])):
        total_winnings += (rank+1) * hand["bid"]
    return total_winnings


# puzzle 1
print(calculate_total_winnings(all_hands))

# puzzle 2
print(calculate_total_winnings(all_hands, True))
