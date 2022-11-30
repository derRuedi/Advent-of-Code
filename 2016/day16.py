'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

# input from website
input = "01110110101001000"


def dragon_curve(a):
    b = "".join("1" if i == "0" else "0" for i in a[::-1])
    return a + "0" + b


def calc_checksum(input):
    while len(input) % 2 == 0:
        input = ["1" if c[0] == c[1] else "0" for c in zip(
            input[::2], input[1::2])]

    print("".join(input))


def gen_start(input, length):
    while len(input) < length:
        input = dragon_curve(input)
    return input[:length]


calc_checksum(gen_start(input, 272))
calc_checksum(gen_start(input, 35651584))
