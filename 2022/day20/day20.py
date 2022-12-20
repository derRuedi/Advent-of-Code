'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/20
'''

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'


def mix(input_file, rounds=1, decryption_key=1):
    with open(input_file, 'r') as f:
        data = [[int(i) * decryption_key, idx]
                for idx, i in enumerate(f.read().splitlines())]

    for _ in range(rounds):
        for id_item_to_move in range(len(data)):
            old_id = None

            for d in data:
                if d[1] == id_item_to_move:
                    old_id = data.index(d)
                    break

            new_id = (old_id + d[0]) % (len(data) - 1)
            data.pop(old_id)
            data.insert(new_id, d)

    zero_item = [d for d in data if d[0] == 0]
    after_0_offset = data.index(zero_item[0])
    print(sum(
        data[(after_0_offset + i) % len(data)][0]for i in [1000, 2000, 3000]))


# part 1
mix(input)

# part 2
decryption_key = 811589153
rounds = 10
mix(input, rounds, decryption_key)
