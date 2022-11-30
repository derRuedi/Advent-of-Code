'''
    Advent of Code Day 4
    https://adventofcode.com/2021/day/4
'''

data = []
with open("day4.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = []
with open("day4.sample_input.txt", "r") as f:
    sample_data = f.read().splitlines()


def create_bingo_cards(bingo_data):
    if len(bingo_data) % 5 != 0:
        print("Input is not divisible by 5. Are you sure your input data is correct?")
    bingo_cards = []

    while len(bingo_data) != 0:
        bingo_card = []
        for i in range(5):
            bingo_card_row = [[int(num), False]
                              for num in bingo_data.pop(0).split()]
            bingo_card.append(bingo_card_row)
        bingo_cards.append(bingo_card)
    return bingo_cards


def update_draw_status(bingo_cards, drawn_number):
    for idx_card, card in enumerate(bingo_cards):
        for idx_line, line in enumerate(card):
            for idx_num, num in enumerate(line):
                if num[0] == drawn_number:
                    bingo_cards[idx_card][idx_line][idx_num][1] = True


def is_winner(bingo_card):
    items_to_check = []

    # add numbers in any row (horizontally)
    items_to_check = [line for line in bingo_card]

    # add numbers in any column (vertically)
    for i in range(len(bingo_card)):
        items_to_check.append(
            [
                bingo_card[0][i],
                bingo_card[1][i],
                bingo_card[2][i],
                bingo_card[3][i],
                bingo_card[4][i]
            ]
        )

    # will check the following items (lines or colums)
    for item in items_to_check:
        if (all(drawn for num, drawn in item)):
            return True
    return False


def check_for_winners(bingo_cards):
    winners = []
    for card in bingo_cards:
        if is_winner(card):
            winners.append(card)
    return winners


def remove_cards(bingo_cards, cards_to_remove):
    for card_to_remove in cards_to_remove:
        for idx, card in enumerate(bingo_cards):
            if card == card_to_remove:
                bingo_cards.pop(idx)


def print_bingo_cards(bingo_cards, show_draw_status=False):
    for card in bingo_cards:
        print_bingo_card(card, show_draw_status)


def print_bingo_card(bingo_card, show_draw_status=False):
    delim = "\t\t" if show_draw_status else "\t"
    print(delim.join(map(str, "BINGO")))
    print(delim.join(map(str, "-----")))
    for line in bingo_card:
        if not show_draw_status:
            line = [num for num, drawn in line]
        print("\t".join(map(str, line)))
    print()


def puzzle1(data):
    draw = [int(i) for i in data[0].split(",")]
    bingo_data = [line for line in data[1:] if line]
    bingo_cards = create_bingo_cards(bingo_data)

    for num in draw:
        update_draw_status(bingo_cards, num)
        winners = check_for_winners(bingo_cards)
        if winners:
            sum = 0
            for line in winners[0]:
                for n, drawn in line:
                    if not drawn:
                        sum += n
            return sum * num


def puzzle2(data):
    draw = [int(i) for i in data[0].split(",")]
    bingo_data = [line for line in data[1:] if line]
    bingo_cards = create_bingo_cards(bingo_data)

    winner_cards = []

    for num in draw:
        update_draw_status(bingo_cards, num)
        winners = check_for_winners(bingo_cards)
        if winners:
            remove_cards(bingo_cards, winners)
            winner_cards.extend(winners)
            last_win_on_drawn_num = num

    loser = winner_cards.pop()
    sum = 0
    for line in loser:
        for n, drawn in line:
            if not drawn:
                sum += n
    return sum * last_win_on_drawn_num


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
