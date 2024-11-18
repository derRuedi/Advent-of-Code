'''
    Advent of Code Day 20
    https://adventofcode.com/2021/day/20
'''
import numpy as np
from termcolor import colored


def process_input_data(filename):
    data = []
    with open(filename, "r") as f:
        data = f.read().splitlines()

    image_enhancement_algorithm = data[0]
    input_image = np.array([list(line) for line in data[2:]])

    return image_enhancement_algorithm, input_image


def create_neighbors():
    neighbors = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            neighbors.append((x, y))
    return neighbors


def enhance_image(input_image, image_enhancement_algorithm, default="."):
    neighbors = create_neighbors()
    input_image = np.pad(input_image, 1, constant_values=default)
    w = len(input_image)
    h = len(input_image[0])
    enhanced_image = np.full((h, w), ".", dtype=str)

    for y in range(h):
        for x in range(w):
            output_pixel_literal = ""
            for neighbor in neighbors:
                check_x = x + neighbor[0]
                check_y = y + neighbor[1]
                if check_x < 0 or check_x >= w or check_y < 0 or check_y >= h:
                    output_pixel_literal += default
                    continue
                output_pixel_literal += input_image[check_y][check_x]
            output_pixel_value = int(output_pixel_literal.replace(
                ".", "0").replace("#", "1"), 2)
            enhanced_image[y][x] = image_enhancement_algorithm[output_pixel_value]
    return enhanced_image


def print_image(image):
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == "#":
                print(colored(image[y][x], "red", attrs=["bold"]), end="")
            else:
                print(image[y][x], end="")
        print()
    print()


def count_lit_pixels(image, lit_pixel="#"):
    count = 0
    for y in range(len(image)):
        for x in range(len(image[0])):
            if image[y][x] == lit_pixel:
                count += 1
    return count


def solve(filename, part2=False):
    image_enhancement_algorithm, input_image = process_input_data(filename)

    iterations = 50 if part2 else 2
    for i in range(iterations):
        if i % 2 != 0 or image_enhancement_algorithm[0] == '.':
            default = image_enhancement_algorithm[0]
        else:
            default = image_enhancement_algorithm[-1]
        enhanced_image = enhance_image(
            input_image, image_enhancement_algorithm, default)
        input_image = enhanced_image

    return count_lit_pixels(enhanced_image)


def puzzle1(filename):
    return solve(filename)


def puzzle2(filename):
    return solve(filename, True)


if __name__ == "__main__":
    assert solve('day20.sample_input.txt') == 35
    assert solve('day20.sample_input.txt', True) == 3351

    print(f"The answer to Puzzle #1 is: {puzzle1('day20.input.txt')}")
    print(f"The answer to Puzzle #2 is: {puzzle2('day20.input.txt')}")
