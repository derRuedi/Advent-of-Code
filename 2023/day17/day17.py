'''
    Advent of Code 2023
    https://adventofcode.com/2023/day/17
'''
import numpy as np
import heapq

# input from website
sample_input = False
input = 'day17_sample.txt' if sample_input else 'day17.txt'
with open(input, 'r') as f:
    data = [[int(i) for i in line] for line in f.read().splitlines()]

puzzle_input = np.array(data)

print(puzzle_input)

right = (0, 1)
down = (1, 0)
left = (0, -1)
up = (-1, 0)


def dijkstra(puzzle_map, min_steps, max_steps):
    visited = set()
    queue = []
    # queue = [(0, 0, 0, right, 1), (0, 0, 0, down, 1)]
    # start at top left, first block does not cost anything
    cost, x, y, direction_count = 0, 0, 0, 1
    # once down
    queue.append((cost, x, y, right, direction_count))
    # once right
    queue.append((cost, x, y, down, direction_count))

    max_x = puzzle_map.shape[1]
    max_y = puzzle_map.shape[0]

    while len(queue) > 0:
        cost, x, y, direction, direction_count = heapq.heappop(queue)
        if (x, y, direction, direction_count) in visited:
            continue
        else:
            visited.add((x, y, direction, direction_count))

        new_x = x + direction[1]
        new_y = y + direction[0]

        # out of bounds
        if new_x < 0 or new_y < 0 or new_x >= max_x or new_y >= max_y:
            continue

        new_cost = cost + puzzle_map[new_y][new_x]

        if direction_count >= min_steps and direction_count <= max_steps:
            # if we are at the end, i.e. bottom right corner
            if new_y == max_y-1 and new_x == max_x-1:
                return new_cost

        # add new steps to queue
        for steps in [right, down, left, up]:
            # if new direction cancels old direction, skip it
            if direction[0] + steps[0] == 0 and direction[1] + steps[1] == 0:
                continue

            # what's our direction count in this direction?
            if direction == steps:
                # new_direction_count = direction_count + 1
                new_direction_count = direction_count + 1
            else:
                # new_direction_count = 1
                new_direction_count = 1

            # if >3, skip it
            if new_direction_count > max_steps:
                continue

            if (direction != steps and direction_count < min_steps):
                continue

            heapq.heappush(
                queue, (new_cost, new_x, new_y, steps, new_direction_count))


print(dijkstra(puzzle_input, 1, 3))
print(dijkstra(puzzle_input, 4, 10))
