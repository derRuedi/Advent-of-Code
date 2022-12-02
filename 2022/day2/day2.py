'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/2
'''

# input from website
with open(f'input.txt', 'r') as f:
    data = [tuple(a.split(" ")) for a in f.read().splitlines()]

# A or X for Rock
# B or Y for Paper
# C or Z for Scissors
winners = [
    ('A', 'Y'),
    ('B', 'Z'),
    ('C', 'X')
]
draws = [
    ('A', 'X'),
    ('B', 'Y'),
    ('C', 'Z')
]

# 0 if you lost, 3 if the round was a draw, 6 if you won
score_lost, score_draw, score_won = 0, 3, 6

# 1 for Rock, 2 for Paper, 3 for Scissors
points = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3,
}

score = 0
for game in data:
    if game in winners:
        score += score_won + points[game[1]]
    elif game in draws:
        score += score_draw + points[game[1]]
    else:
        score += score_lost + points[game[1]]
print(score)

# part 2
score = 0
for game in data:
    if game[1] == "X":  # X means you need to lose
        score += score_lost
        if game[0] == "A":
            score += points["Z"]
        elif game[0] == "B":
            score += points["X"]
        else:
            score += points["Y"]
    elif game[1] == "Y":  # Y means you need to end the round in a draw
        add = score_draw + points[game[0]]
        score += add
    else:  # Z means you need to win
        score += score_won
        if game[0] == "A":
            score += points["Y"]
        elif game[0] == "B":
            score += points["Z"]
        else:
            score += points["X"]
print(score)
