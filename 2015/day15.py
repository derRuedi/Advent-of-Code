'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import timeit
from functools import reduce
import pathlib
import helper

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def mixtures(total):
    mixtures = []
    for i in range(total + 1):
        for j in range(0, total + 1 - i):
            for k in range(0, total + 1 - i - j):
                l = total - i - j - k
                mixtures.append([i, j, k, l])
    return mixtures


def preprocess_data(data):
    i = []
    for line in data:
        l = line.replace(",", "").split(" ")
        i.append([int(i) for i in l[2::2]])
    return i


def score(recipe, max_calories=0):
    capacity = \
        ingredients[0][0] * recipe[0] + \
        ingredients[1][0] * recipe[1] + \
        ingredients[2][0] * recipe[2] + \
        ingredients[3][0] * recipe[3]

    if capacity < 0:
        return 0

    durability = \
        ingredients[0][1] * recipe[0] + \
        ingredients[1][1] * recipe[1] + \
        ingredients[2][1] * recipe[2] + \
        ingredients[3][1] * recipe[3]

    if durability < 0:
        return 0

    flavor = \
        ingredients[0][2] * recipe[0] + \
        ingredients[1][2] * recipe[1] + \
        ingredients[2][2] * recipe[2] + \
        ingredients[3][2] * recipe[3]

    if flavor < 0:
        return 0

    texture = \
        ingredients[0][3] * recipe[0] + \
        ingredients[1][3] * recipe[1] + \
        ingredients[2][3] * recipe[2] + \
        ingredients[3][3] * recipe[3]

    if texture < 0:
        return 0

    calories = \
        ingredients[0][4] * recipe[0] + \
        ingredients[1][4] * recipe[1] + \
        ingredients[2][4] * recipe[2] + \
        ingredients[3][4] * recipe[3]

    if max_calories and calories != max_calories:
        return 0
    return capacity * durability * flavor * texture


def score2(recipe, max_calories=0):
    proportions = [list(map(lambda x: x*multiplier, ingredient_properties))
                   for ingredient_properties, multiplier in zip(ingredients, recipe)]
    cookie = list(reduce((lambda x, y: map(sum, zip(x, y))), proportions))
    calories = cookie.pop()
    score = reduce((lambda x, y: x*y), (i if i > 0 else 0 for i in cookie))
    if max_calories and calories != max_calories:
        return 0
    return score


ingredients = preprocess_data(data)
recipes = mixtures(100)

print(max(map(score, recipes)))
print(max(map(lambda x: score(x, 500), recipes)))


print(max(map(score2, recipes)))
print(max(map(lambda x: score2(x, 500), recipes)))
