'''
    Advent of Code Day 10
    https://adventofcode.com/2021/day/10
'''

data = []
with open("day10.input.txt", "r") as f:
    data = f.read().splitlines()

sample_data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]"
]


def process_input_data(data):
    new_data = []
    for line in data:
        new_data.append([i for i in line])
    return new_data


def match_chunks(data, return_value="total_syntax_error_score"):
    new_data = process_input_data(data)
    incomplete = []
    complete_by_adding = []
    corrupt = []
    corrupt_chars = []
    matching_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    illegal_character_points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    character_points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    for line in new_data:
        stack = []
        line_corrupt = False
        for c in line:
            if c in "([{<":
                stack.append(c)
            elif c in ")]}>":
                if matching_pairs[stack.pop()] == c:
                    continue
                else:
                    corrupt.append(line)
                    corrupt_chars.append(c)
                    line_corrupt = True
                    break
            else:
                print(f"Unexpected character '{c}' in line '{line}'")
        if stack and not line_corrupt:
            incomplete.append(line)
            complete_by_adding.append([matching_pairs[i] for i in stack[::-1]])

    if return_value == "total_syntax_error_score":
        total_syntax_error_score = sum(
            illegal_character_points[i] for i in corrupt_chars)
        return total_syntax_error_score
    elif return_value == "middle_score_completion_score":
        score_completion_string = []
        for completion_string in complete_by_adding:
            score = 0
            for c in completion_string:
                score = (score * 5) + character_points[c]
            score_completion_string.append(score)

        middle_score_completion_score = sorted(score_completion_string)[
            len(score_completion_string)//2]
        return middle_score_completion_score
    else:
        print("Parameter 'return_value' must either be 'total_syntax_error_score' or 'middle_score_completion_score'.")
        return None


def puzzle1(data):
    return match_chunks(data)


def puzzle2(data):
    return match_chunks(data, "middle_score_completion_score")


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
