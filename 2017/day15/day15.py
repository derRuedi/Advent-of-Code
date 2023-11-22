'''
    Advent of Code 2017
    https://adventofcode.com/2017/day/15
'''

# input from website
sample_input = False
input = 'day15_sample.txt' if sample_input else 'day15.txt'
with open(input, 'r') as f:
    data = f.read().splitlines()

a = int(data[0].split()[-1])
b = int(data[1].split()[-1])

a_factor = 16807
b_factor = 48271
divisor = 2147483647


def number_generator(start, factor, divisor, multiples=None):
    value = start * factor % divisor
    while True:
        if multiples:
            if value % multiples == 0:
                yield value
        else:
            yield value
        value = value * factor % divisor


def dec_to_bin(dec: int, length=0) -> str:
    '''Return binary representation (string without prefix) of given decimal.'''
    if length:
        return format(dec, f'0{length}b')
    return format(dec, 'b')


a_gen = number_generator(a, a_factor, divisor)
b_gen = number_generator(b, b_factor, divisor)


pairs = 40_000_000
c = 0
for i in range(pairs):
    if dec_to_bin(next(a_gen), 16)[-16:] == dec_to_bin(next(b_gen), 16)[-16:]:
        c += 1
print(c)


a_gen = number_generator(a, a_factor, divisor, 4)
b_gen = number_generator(b, b_factor, divisor, 8)

pairs = 5_000_000
c = 0
for i in range(pairs):
    if dec_to_bin(next(a_gen), 16)[-16:] == dec_to_bin(next(b_gen), 16)[-16:]:
        c += 1
print(c)
