'''
    Advent of Code Day 1
    https://adventofcode.com/2021/day/1
'''

# input from website in raw format
data = []
with open('day1.input.txt', 'r') as f:
    data = [int(i) for i in f.read().splitlines()]

sample_data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]


def puzzle1(data):
    i = 1
    count = 0
    while i < len(data):
        if data[i] > data[i-1]:
            count += 1
        i += 1
    return count


def puzzle2(data):
    sliding_window = zip(data, data[1:], data[2:])
    sliding_window = [sum(i) for i in sliding_window]
    return puzzle1(sliding_window)


def puzzle2_2(data):
    i = 1
    sliding_window = []
    while i < len(data) - 1:
        sliding_window.append(data[i-1] + data[i] + data[i+1])
        i += 1
    return puzzle1(sliding_window)


def check_performance(fn, *param):
    """Simple function to calculate and display the time it takes to complete a function call."""
    from time import perf_counter
    start_time = perf_counter()
    fn(*param)
    end_time = perf_counter()
    print(
        f'It took {end_time - start_time: 0.5} second(s) to complete {fn.__name__}.')


print(f"The answer to Puzzle #1's sample data is: {puzzle1(sample_data)}")
print(f"The answer to Puzzle #1 is: {puzzle1(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2(data)}")

print(f"The answer to Puzzle #2's sample data is: {puzzle2_2(sample_data)}")
print(f"The answer to Puzzle #2 is: {puzzle2_2(data)}")
