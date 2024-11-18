'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


def preprocess_data(data):
    wires = {}
    # signal, wire, gate, another wire, some specific value
    for d in data:
        instruction = d.split(" ")
        match len(instruction):
            case 5:
                # something with a gate, e.g.: af AND ah -> ai
                wires[instruction[-1]] = instruction[0:3]
            case 4:
                # bitwise complement, e.g.: NOT go -> gp
                wires[instruction[-1]] = instruction[0:2]
            case 3:
                # signal input, e.g.: 14146 -> b
                wires[instruction[-1]] = instruction[0:1]
    return wires


def flatten(l):
    '''Flatten two dimensional list and return one dimensional list.'''
    return [item for sublist in l for item in sublist]


def bin_to_dec(bin: str) -> int:
    '''Return decimal value of given binary string.'''
    return int(str(bin), 2)


def dec_to_bin(dec, length=0) -> str:
    '''Return binary representation (string without prefix) of given decimal.'''
    if type(dec) == list:
        dec = int(dec[0])
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


def evaluate(expression, wires):
    if expression.isnumeric():
        return int(expression)
    match len(wires[expression]):
        case 1:
            # if we have a numeric signal for a given wire
            if wires[expression][0].isnumeric():
                wires[expression] = [wires[expression][0]]
                return int(wires[expression][0])
            # if we have another wire connected to a given wire
            elif wires[expression][0] in wires:
                wires[expression] = evaluate(wires[expression][0], wires)
                return wires[expression]
            else:
                print(f"Something wrong in lookup: {wires[expression]}")
                return None
        case 2:
            wires[expression] = [str(bitwise_complement(
                evaluate(wires[expression][1], wires), 16))]
            return wires[expression]

        case 3:
            match wires[expression][1]:
                case "AND":
                    wires[expression] = [str(bitwise_and(
                        evaluate(wires[expression][0], wires),
                        evaluate(wires[expression][2], wires), 16))]
                    return wires[expression]
                case "OR":
                    wires[expression] = [str(bitwise_or(
                        evaluate(wires[expression][0], wires),
                        evaluate(wires[expression][2], wires), 16))]
                    return wires[expression]
                case "LSHIFT":
                    wires[expression] = [str(bitwise_lshift(
                        evaluate(wires[expression][0], wires),
                        int(wires[expression][2]), 16))]
                    return wires[expression]
                case "RSHIFT":
                    wires[expression] = [str(bitwise_rshift(
                        evaluate(wires[expression][0], wires),
                        int(wires[expression][2]), 16))]
                    return wires[expression]


def puzzle(data):
    wires = preprocess_data(data)

    # for k, v in wires.items():
    #     print(f"wires[{k}] = {v}")
    # print()

    # print(evaluate("d", wires))
    # print(evaluate("e", wires))
    # print(evaluate("f", wires))
    # print(evaluate("g", wires))
    # print(evaluate("h", wires))
    # print(evaluate("i", wires))
    # print(evaluate("x", wires))
    # print(evaluate("y", wires))

    print(evaluate("a", wires))


puzzle(data)
