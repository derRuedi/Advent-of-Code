'''
    Advent of Code Day 16
    https://adventofcode.com/2021/day/16
'''

data = []
with open("day16.input.txt", "r") as f:
    data = f.read().splitlines()


def hex_to_binary(data):
    new_data = ""
    for c in data[0]:
        new_data += bin(int(c, 16))[2:].zfill(4)
    return new_data


def decode_transmission(transmission, i=0):
    # return { "version": None, "type": None, "value": None, "sub_packets": [] }, i
    packet_version = int(transmission[i:i+3], 2)
    i += 3
    packet_type_id = int(transmission[i:i+3], 2)
    i += 3
    # literal packet
    if packet_type_id == 4:
        value, i = get_literal_value(transmission, i)
        sub_packets = []
    # operator packet
    else:
        length_type_id = int(transmission[i:i+1])
        i += 1
        if length_type_id == 0:
            sub_packets, i = get_sub_packets_by_length(transmission, i)
        else:
            sub_packets, i = get_sub_packets_by_number(transmission, i)
        value = calculate_value(packet_type_id, sub_packets)
    return {"version": packet_version, "type": packet_type_id, "value": value, "sub_packets": sub_packets}, i


def get_literal_value(transmission, i):
    literal = ""
    substring = transmission[i:i+5]
    i += 5
    literal += substring[1:]
    leftover_bits = 0
    while substring[0] == "1":
        substring = transmission[i:i+5]
        i += 5
        literal += substring[1:]
        leftover_bits += 1
    # leftover_bits = (4 - leftover_bits) % 4
    return int(literal, 2), i


def get_sub_packets_by_length(transmission, i):
    length_of_sub_packets = int(transmission[i:i+15], 2)
    sub_packets = []
    i += 15
    length_decoded = 0
    while length_decoded < length_of_sub_packets:
        sub_packet, j = decode_transmission(transmission, i)
        sub_packets.append(sub_packet)
        length_decoded += j - i
        i = j
    return sub_packets, i


def get_sub_packets_by_number(transmission, i):
    number_of_sub_packets = int(transmission[i:i+11], 2)
    i += 11
    sub_packets = []
    for _ in range(number_of_sub_packets):
        sub_packet, j = decode_transmission(transmission, i)
        sub_packets.append(sub_packet)
        i = j
    return sub_packets, i


def calculate_value(packet_type_id, sub_packets):
    values = [sub_packet["value"] for sub_packet in sub_packets]
    if packet_type_id == 0:
        return sum(values)
    elif packet_type_id == 1:
        product = values[0]
        if values[1:]:
            for p in values[1:]:
                product *= p
        return product
    elif packet_type_id == 2:
        return min(values)
    elif packet_type_id == 3:
        return max(values)
    elif packet_type_id == 5:
        return int(values[0] > values[1])
    elif packet_type_id == 6:
        return int(values[0] < values[1])
    elif packet_type_id == 7:
        return int(values[0] == values[1])
    else:
        print("SOMETHING WRONG HERE!")


def sum_versions(packet):
    # packet = { "version": None, "type": None, "value": None, "sub_packets": [] }, i
    result = packet["version"]
    for p in packet["sub_packets"]:
        result += sum_versions(p)
    return result


def puzzle1(data):
    transmission = hex_to_binary(data)
    packet, i = decode_transmission(transmission, 0)
    return sum_versions(packet)


def puzzle2(data):
    transmission = hex_to_binary(data)
    packet, i = decode_transmission(transmission, 0)
    return packet["value"]


if __name__ == "__main__":

    assert puzzle1(["D2FE28"]) == 6
    assert puzzle1(["8A004A801A8002F478"]) == 16
    assert puzzle1(["620080001611562C8802118E34"]) == 12
    assert puzzle1(["C0015000016115A2E0802F182340"]) == 23
    assert puzzle1(["A0016C880162017C3686B18A3D4780"]) == 31

    assert puzzle2(["D2FE28"]) == 2021
    assert puzzle2(["C200B40A82"]) == 3
    assert puzzle2(["04005AC33890"]) == 54
    assert puzzle2(["880086C3E88112"]) == 7
    assert puzzle2(["CE00C43D881120"]) == 9
    assert puzzle2(["D8005AC2A8F0"]) == 1
    assert puzzle2(["F600BC2D8F"]) == 0
    assert puzzle2(["9C005AC2F8F0"]) == 0
    assert puzzle2(["9C0141080250320F1802104A08"]) == 1

    print(f"The answer to Puzzle #1 is: {puzzle1(data)}")
    print(f"The answer to Puzzle #2 is: {puzzle2(data)}")
