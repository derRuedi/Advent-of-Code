'''
    Advent of Code Day XX
    https://adventofcode.com/2021/day/XX
'''

data = "target area: x=230..283, y=-107..-57"

sample_data = "target area: x=20..30, y=-10..-5"


def process_input_data(data):
    x, y = data[13:].split(", ")
    x_min, x_max = x[2:].split("..")
    y_min, y_max = y[2:].split("..")
    target_area = {}
    target_area["x_min"] = int(x_min)
    target_area["x_max"] = int(x_max)
    target_area["y_min"] = int(y_min)
    target_area["y_max"] = int(y_max)
    return target_area


def probe(start_position, x_velocity, y_velocity, target_area):
    x_pos = start_position[0]
    y_pos = start_position[1]
    positions = [(x_pos, y_pos)]
    step = 0
    while y_pos > target_area["y_min"]:
        # The probe's x position increases by its x velocity.
        x_pos += x_velocity
        # Due to drag, the probe's x velocity changes by 1 toward the value 0.
        if x_velocity > 0:
            x_velocity = x_velocity - 1
        elif x_velocity < 0:
            x_velocity = x_velocity + 1
        # The probe's y position increases by its y velocity.
        y_pos += y_velocity
        # Due to gravity, the probe's y velocity decreases by 1.
        y_velocity = y_velocity - 1
        new_pos = (x_pos, y_pos)
        positions.append(new_pos)
        if is_point_in_target_area(new_pos, target_area):
            return positions

    # Probe does not hit target area
    return None


def is_point_in_target_area(point, target_area):
    x, y = point
    if (x >= target_area["x_min"] and x <= target_area["x_max"]) and (
            y >= target_area["y_min"] and y <= target_area["y_max"]):
        return True
    return False


def calculate_possible_x_values(target_area):
    i, s = 0, 0
    while s <= target_area["x_min"]:
        i += 1
        s += i
    possible_x_values = list(range(i, abs(target_area["x_max"])+1))
    return possible_x_values


def calculate_possible_y_values(target_area):
    possible_y_values = list(
        range(-abs(target_area["y_min"]), abs(target_area["y_min"])))
    return possible_y_values


def answer(data):
    target_area = process_input_data(data)

    possible_x_values = calculate_possible_x_values(target_area)
    possible_y_values = calculate_possible_y_values(target_area)
    probes = [(x, y) for x in possible_x_values for y in possible_y_values]

    max_y = 0
    results = 0
    for p in probes:
        # print(f"probing {p[0]}, {p[1]} - ", end="")
        positions = probe((0, 0), p[0], p[1], target_area)
        # print(f"{True if positions else False}")
        if positions:
            results += 1
            max_y_positions = max(p[1] for p in positions)
            if max_y_positions > max_y:
                max_y = max_y_positions

    print(f"The answer to Puzzle #1 is: {max_y}")
    print(f"The answer to Puzzle #2 is: {results}")


# answer(sample_data)
answer(data)
