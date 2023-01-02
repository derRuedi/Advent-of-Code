'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/25
'''

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()


snafu_decimal = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

decimal_snafu = {v: k for k, v in snafu_decimal.items()}


def snafu_to_decimal(number):
    return sum(snafu_decimal[d] * 5 ** i for i, d in enumerate(reversed(number)))


def decimal_to_snafu(number):
    if number:
        quotient, remainder = divmod(number+2, 5)
        return decimal_to_snafu(quotient) + decimal_snafu[remainder-2]
    else:
        return ''


assert 1 == snafu_to_decimal("1")
assert 2 == snafu_to_decimal("2")
assert 3 == snafu_to_decimal("1=")
assert 4 == snafu_to_decimal("1-")
assert 5 == snafu_to_decimal("10")
assert 6 == snafu_to_decimal("11")
assert 7 == snafu_to_decimal("12")
assert 8 == snafu_to_decimal("2=")
assert 9 == snafu_to_decimal("2-")
assert 10 == snafu_to_decimal("20")
assert 15 == snafu_to_decimal("1=0")
assert 20 == snafu_to_decimal("1-0")
assert 2022 == snafu_to_decimal("1=11-2")
assert 12345 == snafu_to_decimal("1-0---0")
assert 314159265 == snafu_to_decimal("1121-1110-1=0")

assert decimal_to_snafu(1) == "1"
assert decimal_to_snafu(2) == "2"
assert decimal_to_snafu(3) == "1="
assert decimal_to_snafu(4) == "1-"
assert decimal_to_snafu(5) == "10"
assert decimal_to_snafu(6) == "11"
assert decimal_to_snafu(7) == "12"
assert decimal_to_snafu(8) == "2="
assert decimal_to_snafu(9) == "2-"
assert decimal_to_snafu(10) == "20"
assert decimal_to_snafu(15) == "1=0"
assert decimal_to_snafu(20) == "1-0"
assert decimal_to_snafu(2022) == "1=11-2"
assert decimal_to_snafu(12345) == "1-0---0"
assert decimal_to_snafu(314159265) == "1121-1110-1=0"


snafu_sum = 0
for number in data:
    snafu_sum += snafu_to_decimal(number)

print(snafu_sum)
print(decimal_to_snafu(snafu_sum))
