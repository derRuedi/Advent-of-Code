'''
    Advent of Code Day 8
    https://adventofcode.com/2021/day/8
'''

data = []
with open("day8.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]


def process_input_data(data):
    new_data = []
    for line in data:
        unique_signal_patterns, digit_output_values = line.split("|")
        new_data.append([unique_signal_patterns.split(),
                        digit_output_values.split()])
    return new_data


def create_mapping(unique_signal_patterns):
    unique_signal_patterns.sort(key=lambda x: len(x))
    seven_segment_display = {}
    # 1 is len() = 2
    seven_segment_display[1] = list(unique_signal_patterns.pop(0))
    # 7 is len() = 3
    seven_segment_display[7] = list(unique_signal_patterns.pop(0))
    # 4 is len() = 4
    seven_segment_display[4] = list(unique_signal_patterns.pop(0))
    # 8 is len() = 7
    seven_segment_display[8] = list(unique_signal_patterns.pop())

    # all 5-letter digits
    two_three_five = unique_signal_patterns[:3]

    # 3 is the one in '2', '3' or '5' that contains '1'
    for idx, candidate in enumerate(two_three_five):
        if all([True if x in candidate else False for x in seven_segment_display[1]]):
            break
    seven_segment_display[3] = list(two_three_five.pop(idx))

    # L-element is '4' - '1'
    helper = [x for x in seven_segment_display[4]
              if x not in seven_segment_display[1]]
    # 5 is the one in '2', '3' or '5' that contains the L-element
    for idx, candidate in enumerate(two_three_five):
        if all([True if x in candidate else False for x in helper]):
            break
    seven_segment_display[5] = list(two_three_five.pop(idx))

    # 2 is the remainder in two_three_five
    seven_segment_display[2] = list(two_three_five.pop())

    # all 6-letter digits
    six_nine_zero = unique_signal_patterns[3:]

    # 9 is the one in '6', '9' or '0' that contains '4'
    for idx, candidate in enumerate(six_nine_zero):
        if all([True if x in candidate else False for x in seven_segment_display[4]]):
            break
    seven_segment_display[9] = list(six_nine_zero.pop(idx))

    # 6 is the one in '6', '9' or '0' that contains the L-element
    for idx, candidate in enumerate(six_nine_zero):
        if all([True if x in candidate else False for x in helper]):
            break
    seven_segment_display[6] = list(six_nine_zero.pop(idx))

    # 0 is the remainder in six_nine_zero
    seven_segment_display[0] = list(six_nine_zero.pop())

    mapping = {}
    for i in range(10):
        mapping["".join(sorted(seven_segment_display[i]))] = i

    return mapping


def puzzle1(data):
    seven_segment_display = {
        0: "abcefg",
        1: "cf",        #
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",      #
        5: "abdfg",
        6: "abdefg",
        7: "acf",       #
        8: "abcdefg",   #
        9: "abcdfg",
    }

    s = set()
    for number in [1, 4, 7, 8]:
        s.add(len(seven_segment_display[number]))
    unique_number_of_segments = []

    new_data = process_input_data(data)
    for line in new_data:
        digit_output_values = line[1]
        for digit_output_value in digit_output_values:
            if len(digit_output_value) in s:
                unique_number_of_segments.append(digit_output_value)

    return len(unique_number_of_segments)


def puzzle2(data):
    new_data = process_input_data(data)
    sum = 0
    for line in new_data:
        unique_signal_patterns = line[0]
        digit_output_values = line[1]
        mapping = create_mapping(unique_signal_patterns)
        num = [mapping["".join(sorted(x))] for x in digit_output_values]
        num = int("".join(map(str, num)))
        sum += num
    return sum


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
