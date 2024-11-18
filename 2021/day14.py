'''
    Advent of Code Day 14
    https://adventofcode.com/2021/day/14
'''

from collections import defaultdict

data = []
with open("day14.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C"
]


def process_input_data(data):
    polymer_template = data[0]
    pair_insertion_rules = {}
    for line in data[2:]:
        k, v = line.split(" -> ")
        pair_insertion_rules[k] = v
    return polymer_template, pair_insertion_rules


def create_pairs(string):
    pairs = []
    for i in range(1, len(string)):
        pairs.append(str(string[i-1] + string[i]))
    return pairs


def polymerization(polymer_template, pair_insertion_rules, steps):
    polymer = polymer_template
    for _ in range(steps):
        pairs = create_pairs(polymer)
        new_polymer = ""
        for pair in pairs:
            insert = pair[0] + pair_insertion_rules[pair]
            new_polymer = new_polymer + insert
        new_polymer = new_polymer + pair[1]
        polymer = new_polymer

    occurences = {}
    for element in polymer:
        if element not in occurences.keys():
            occurences[element] = 1
        else:
            occurences[element] += 1

    occurences_values = occurences.values()
    return max(occurences_values) - min(occurences_values)


def polymerization_optimized(polymer_template, pair_insertion_rules, steps):
    pair_count = defaultdict(int)
    character_count = defaultdict(int)

    # initialize pair_count with polymer_template
    for i in range(1, len(polymer_template)):
        pair_count[polymer_template[i-1] + polymer_template[i]] += 1

    # initialize character_count with polymer_template
    for c in polymer_template:
        character_count[c] += 1

    for _ in range(steps):
        new_pair_count = defaultdict(int)

        for pair in list(pair_count):
            # example pair = "CH"
            # splitting "CH" creates "CBH"
            # the new character needs to be accounted for as many times as the pair is present in the pair count
            character_count[pair_insertion_rules[pair]] += pair_count[pair]
            # every occurence of "the _new_ left part" ("CB" in the example) of the newly created pair
            # needs to be increased by the amount of the pair present in the pair count
            new_pair_count[pair[0] +
                           pair_insertion_rules[pair]] += pair_count[pair]
            # and every occurence of "the _new_ right part" ("BH" in the example) of the newly created pair
            # needs to be increased by the amount of the pair present in the pair count
            new_pair_count[pair_insertion_rules[pair] +
                           pair[1]] += pair_count[pair]

        pair_count = new_pair_count

    character_count_values = character_count.values()
    return max(character_count_values) - min(character_count_values)


def puzzle1(data):
    polymer_template, pair_insertion_rules = process_input_data(data)
    return polymerization(polymer_template, pair_insertion_rules, 10)


def puzzle2(data):
    polymer_template, pair_insertion_rules = process_input_data(data)
    return polymerization_optimized(polymer_template, pair_insertion_rules, 40)


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
