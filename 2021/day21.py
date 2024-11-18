'''
    Advent of Code Day 21
    https://adventofcode.com/2021/day/21
'''

data = []
with open("day21.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "Player 1 starting position: 4",
    "Player 2 starting position: 8"
]


class Die:
    def __init__(self):
        self.rolled = 0

    def triangular_number(n):
        return n * (n + 1) // 2

    def roll(self):
        result = 0
        for i in range(3):
            n = (self.rolled - (self.rolled // 100)*100)+1
            self.rolled += 1
            result += n
        return result


def initialize(data):
    p1 = {
        "name": "p1",
        "pos": int(data[0][-1]),
        "score": 0
    }
    p2 = {
        "name": "p2",
        "pos": int(data[1][-1]),
        "score": 0
    }
    die = Die()
    return die, p1, p2


def puzzle1(data):
    die, p1, p2 = initialize(data)
    loser = None
    while p1["score"] < 1000 and p2["score"] < 1000:
        for p in [p1, p2]:
            p_movs = die.roll()
            new_pos = p["pos"] + p_movs % 10
            if new_pos > 10:
                new_pos -= 10
            p["pos"] = new_pos
            p["score"] += p["pos"]
            if p["score"] >= 1000:
                if p == p1:
                    loser = p2
                else:
                    loser = p1
                break
    return die.rolled * loser["score"]


def puzzle2(data):
    pass


if __name__ == "__main__":

    # assertions go here
    assert puzzle1(sample_data) == 739785
    assert puzzle2(sample_data) == 444356092776315

    print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

    # print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
    # print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
