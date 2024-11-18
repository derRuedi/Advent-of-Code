

import math


def flatten(l):
    '''Flatten two dimensional list and return one dimensional list.'''
    return [item for sublist in l for item in sublist]


def bin_to_dec(bin) -> int:
    '''Return decimal value of given binary string.'''
    return int(str(bin), 2)


def dec_to_bin(dec: int, length=0) -> str:
    '''Return binary representation (string without prefix) of given decimal.'''
    if length:
        return format(dec, f'0{length}b')
    return format(dec, 'b')


def bitwise_complement(dec: int, length=0) -> int:
    bitwise_complement_binary = \
        "".join(["1" if i == "0" else "0" for i in dec_to_bin(dec, length)])
    return int(str(bitwise_complement_binary), 2)


def bitwise_and(dec1: int, dec2: int, length=0) -> int:
    binary1 = dec_to_bin(dec1, length)
    binary2 = dec_to_bin(dec2, length)
    bitwise_and_binary = ""
    for i, x in enumerate(binary1):
        if binary1[i] == "1" and binary2[i] == "1":
            bitwise_and_binary += "1"
        else:
            bitwise_and_binary += "0"
    return int(str(bitwise_and_binary), 2)


def bitwise_or(dec1, dec2, length=0) -> int:
    binary1 = dec_to_bin(dec1, length)
    binary2 = dec_to_bin(dec2, length)
    bitwise_and_binary = ""
    for i, x in enumerate(binary1):
        if binary1[i] == "1" or binary2[i] == "1":
            bitwise_and_binary += "1"
        else:
            bitwise_and_binary += "0"
    return int(str(bitwise_and_binary), 2)


def bitwise_lshift(dec: int, amount: int, length=0) -> int:
    binary = dec_to_bin(dec, length)
    bitwise_lshift = binary[amount:] + amount*"0"
    return int(str(bitwise_lshift), 2)


def bitwise_rshift(dec: int, amount: int, length=0) -> int:
    binary = dec_to_bin(dec, length)
    bitwise_rshift = amount*"0" + binary[:-amount]
    return int(str(bitwise_rshift), 2)


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def mixtures(n, total):
    '''
    generates combinations with a total sum
    e.g. mixtures(2, 10) produces:
    [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0]]
    '''
    start = total if n == 1 else 0

    for i in range(start, total+1):
        left = total - i
        if n-1:
            for y in mixtures(n-1, left):
                yield [i] + y
        else:
            yield [i]


def replace_nth(string, old, new, n):
    '''
    replace n-th substring in a string
    '''
    parts = string.split(old)
    if n >= len(parts):
        return None
    left = parts[0:n]
    right = parts[n:]
    return old.join(left) + new + old.join(right)


def sum_div(n):
    '''
    divisor function sigma_1
    https://en.wikipedia.org/wiki/Divisor_function
    '''
    if (n == 1):
        return 1

    # Final result of summation
    # of divisors
    result = 0

    # find all divisors which
    # divides 'num'
    for i in range(2, (int)(math.sqrt(n))+1):

        # if 'i' is divisor of 'n'
        if (n % i == 0):

            # if both divisors are same
            # then add it only once
            # else add both
            if (i == (n/i)):
                result = result + i
            else:
                result = result + (i + n//i)

    # Add 1 and n to result as above
    # loop considers proper divisors
    # greater than 1.
    return (result + n + 1)


if __name__ == "__main__":
    # print(bitwise_and(15768, 14768, 16))
    # print(bitwise_rshift(23, 5, 16))
    # print(list(mixtures(2, 10)))
    string = "AnnnnnAiiiiiiiAooooooooA"
    print(string)
    r = replace_nth(string, "A", "B", 4)
    print(r)
