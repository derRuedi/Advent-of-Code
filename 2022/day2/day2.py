'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/2
'''

from itertools import product

# input from website
with open(f'input.txt', 'r') as f:
    data = [tuple(a.split(" ")) for a in f.read().splitlines()]

# A for Rock
# B for Paper
# C for Scissors
winners = {
    ('A', 'B'),  # paper beats rock
    ('B', 'C'),  # scissors cut paper
    ('C', 'A')  # rock breaks scissors
}
draws = {
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C')
}
defeats = set(product(["A", "B", "C"], repeat=2)) - winners - draws


# 0 if you lost, 3 if the round was a draw, 6 if you won
score_lost, score_draw, score_won = 0, 3, 6

# 1 for Rock, 2 for Paper, 3 for Scissors
points = {
    "A": 1,
    "B": 2,
    "C": 3
}

score = 0
for game in data:
    # substitute X, Y, Z for A, B, C, respectively
    game = (game[0], "A" if game[1] == "X" else "B" if game[1] == "Y" else "C")
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
    if game[1] == "X":  # lose
        score += score_lost + \
            points[[b for a, b in defeats if a == game[0]][0]]
    elif game[1] == "Y":  # draw
        score += score_draw + points[game[0]]
    else:  # win
        score += score_won + points[[b for a, b in winners if a == game[0]][0]]
print(score)
