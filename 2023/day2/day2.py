'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/2
'''

# input from website
from functools import reduce
sample_input = False
input = 'day2_sample.txt' if sample_input else 'day2.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

# preprocess data
games_data = {}
for line in data:
    game, draws = line.split(":")
    game_id = int(game.split()[1])

    games_data[game_id] = []
    draws = [[a.strip() for a in draw.split(",")] for draw in draws.split(";")]

    for draw in draws:
        games_data[game_id].append({col: int(n)
                                    for d in draw for n, col in [d.split()]})


# puzzle 1
prerequisite = {
    "red": 12,
    "green": 13,
    "blue": 14
}

impossible_games = set()
for game_id, games in games_data.items():
    for game in games:
        for p_col, p_num in prerequisite.items():
            if p_col in game.keys() and game[p_col] > prerequisite[p_col]:
                impossible_games.add(game_id)

possible_games = [game_id for game_id in games_data.keys()
                  if game_id not in impossible_games]
print(sum(possible_games))


# puzzle 2
powers = []
for game_id, games in games_data.items():
    min_cubes_required = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for game in games:
        # print(game_id, game)
        for col, num in min_cubes_required.items():
            if col in game.keys() and game[col] > min_cubes_required[col]:
                min_cubes_required[col] = game[col]
    # print(min_cubes_required)
    powers.append(reduce(lambda a, b: a*b, min_cubes_required.values()))
    # print()

print(sum(powers))
