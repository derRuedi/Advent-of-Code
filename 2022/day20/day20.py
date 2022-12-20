'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/20
'''

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = [[int(i), False] for i in f.read().splitlines()]

while not all(d[1] for d in data):
    # find the first number that has not been moved
    for i in range(len(data)):
        if not data[i][1]:
            break
    # move the number
    number = data.pop(i)
    number[1] = True
    data.insert((i+number[0]) % len(data), number)

# grove coordinates can be found by looking at the
# 1000th, 2000th, and 3000th numbers after the value 0
after_0_offset = data.index([0, True])
print(sum(
    data[(after_0_offset + i) % len(data)][0]for i in [1000, 2000, 3000]))


# part 2
# while solving part 2 I realized, that it is not necessary to explicitly (True/False) keep track,
# if a number has been moved already
# while reading the input, just take the order of the numbers into account and work from that order
decryption_key = 811589153
with open(input, 'r') as f:
    data = [[int(i) * decryption_key, idx]
            for idx, i in enumerate(f.read().splitlines())]

for _ in range(10):
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
