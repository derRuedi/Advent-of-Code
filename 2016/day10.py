'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib
import re

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()

comparing = [17, 61]

# use sample data
if False:
    data = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
""".splitlines()
    comparing = [2, 5]

bot_configurations = []
instructions = []

bots = {}

for line in data:
    if line.startswith("value"):
        instructions.append([int(x) for x in re.findall(r"\d+", line)])
    else:
        bot_configurations.append(line.replace(" ", "").replace(
            "giveslowto", " ").replace("andhighto", " ").split(" "))


for bc in bot_configurations:
    bots[bc[0]] = {
        "low": bc[1],
        "high": bc[2],
        "chips": [],
        "compared": []
    }
    if bc[1].startswith("output"):
        bots[bc[1]] = {"chips": []}
    if bc[2].startswith("output"):
        bots[bc[2]] = {"chips": []}

for i in instructions:
    bots[f"bot{i[1]}"]["chips"].append(i[0])

# as long as there are bots with two chips
while any(details["chips"] for details in [v for k, v in bots.items() if k.startswith("bot")] if len(details["chips"]) == 2):
    for bot, details in bots.items():
        if len(details["chips"]) == 2:
            details["chips"].sort()
            low, high = details["chips"]
            details["chips"].clear()

            bots[details["low"]]["chips"].append(low)
            bots[details["high"]]["chips"].append(high)

            details["compared"].extend([low, high])

# puzzle 1
for bot, details in bots.items():
    if bot.startswith("bot") and details["compared"] == comparing:
        print(bot[3:])

# puzzle 2
print(bots["output0"]["chips"][0] * bots["output1"]
      ["chips"][0] * bots["output2"]["chips"][0])
