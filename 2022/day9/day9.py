'''
    Advent of Code 2022
    https://adventofcode.com/2022/day/9
'''

# input from website
sample_input = False
input = 'sample_input.txt' if sample_input else 'input.txt'
with open(input, 'r') as f:
    data = [l.split() for l in f.read().splitlines()]

directions = {
    "U": (0, +1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (+1, 0),
}

rope_moves = {
    (0, +2): (0, +1),  # head above tail
    (0, -2): (0, -1),  # head below tail
    (-2, 0): (-1, 0),  # head left of tail
    (+2, 0): (+1, 0),  # head right of tail

    (+1, +2): (+1, +1),  # head right above tail
    (-1, +2): (-1, +1),  # head left above tail
    (+1, -2): (+1, -1),  # head right below tail
    (-1, -2): (-1, -1),  # head left below tail

    (+2, +1): (+1, +1),  # head far right above tail
    (-2, +1): (-1, +1),  # head far left above tail
    (+2, -1): (+1, -1),  # head far right below tail
    (-2, -1): (-1, -1),  # head far left below tail

    # moves for part 2
    (+2, +2): (+1, +1),  # head far right far above tail
    (-2, +2): (-1, +1),  # head far left far above tail
    (+2, -2): (+1, -1),  # head far right far below tail
    (-2, -2): (-1, -1),  # head far left far below tail
}

H = [[0, 0] for _ in range(10)]
# for part 1 'T' is equivalent to H[1]
# for part 2 'T' is equivalent to H[9]
visited_positions = [{tuple(H[i])} for i in range(10)]

for motion in data:
    direction = directions[motion[0]]
    steps = int(motion[1])

    for _ in range(1, steps+1):
        H[0][0] += direction[0]
        H[0][1] += direction[1]
        for i in range(1, 10):

            for head_move in rope_moves:
                if H[i][0] + head_move[0] == H[i-1][0] and H[i][1] + head_move[1] == H[i-1][1]:
                    break
            else:
                head_move = None

            if head_move:
                H[i][0] += rope_moves[head_move][0]
                H[i][1] += rope_moves[head_move][1]
                visited_positions[i].add(tuple(H[i]))

print(len(visited_positions[1]))  # part 1
print(len(visited_positions[9]))  # part 2
