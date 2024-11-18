'''
    Advent of Code Day 6
    https://adventofcode.com/2021/day/6
'''

data = []
with open("day6.input.txt", "r") as f:
    data = [int(i) for i in f.read().splitlines()[0].split(",")]

sample_data = [3, 4, 3, 1, 2]

# class Lanternfish:
#     """A simple class to mimic lanternfish."""

#     days_to_recreate = 6

#     def __init__(self, days_to_spawn):
#         self.days_to_spawn = days_to_spawn

#     def __repr__(self):
#         return str(self.days_to_spawn)

#     def tick_tock(self):
#         if self.days_to_spawn == 0:
#             self.days_to_spawn = Lanternfish.days_to_recreate
#             return True
#         else:
#             self.days_to_spawn -= 1
#             return False


# def puzzle1(data):
#     school_of_fish = []
#     for days_to_spawn in data:
#         school_of_fish.append(Lanternfish(days_to_spawn))

#     for i in range(80):
#         for fish in school_of_fish:
#             if fish.tick_tock():
#                 school_of_fish.append(Lanternfish(9))
#     return len(school_of_fish)


def calculate_fish_population(starting_fish_configuration, days):
    school_of_fish = {}
    for i in range(9):
        school_of_fish[i] = 0

    for fish in starting_fish_configuration:
        school_of_fish[fish] += 1

    for i in range(days):
        new_fishes = school_of_fish[0]
        for i in range(8):
            school_of_fish[i] = school_of_fish[i+1] + \
                (new_fishes if i == 6 else 0)
        school_of_fish[8] = new_fishes

    return sum(school_of_fish.values())


def puzzle1(data):
    return calculate_fish_population(data, 80)


def puzzle2(data):
    return calculate_fish_population(data, 256)


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
