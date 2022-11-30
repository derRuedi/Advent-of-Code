'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import pathlib

# input from website in raw format
# auto generate the filename of the input file
# i.e. from python file "dayX.py" it will expect the input file to be named "dayX.input.txt"
with open(f'{pathlib.PurePath(__file__).stem}.input.txt', 'r') as f:
    data = f.read().splitlines()


sum_sector_ids = 0


def is_real_room(room, checksum):
    test = {c: room.count(c) for c in checksum if room.count(c) > 0}
    # the lambda sorts first on the character counts, then on the character itself
    return sorted(test, key=lambda x: (-test[x], x)) == list(checksum)


valid_rooms = []

for line in data:
    tmp = line.split("[")
    checksum = tmp[1][0:-1]
    tmp = tmp[0].split("-")
    sector_id = int(tmp[-1])
    room = "-".join(tmp[0:-1])
    if is_real_room(room, checksum):
        sum_sector_ids += sector_id
        valid_rooms.append((room, sector_id))
print(sum_sector_ids)


for v in valid_rooms:
    sentence = ""
    for c in v[0]:
        if c == "-":
            sentence += " "
        else:
            sentence += chr((ord(c) + v[1] - 97) % 26 + 97)
    if sentence == "northpole object storage":
        print(v[1])
        break
