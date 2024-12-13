'''
    Advent of Code 2024
    https://adventofcode.com/2024/day/5
'''

# input from website
from collections import defaultdict
sample_input = False
input = 'day5_sample.txt' if sample_input else 'day5.txt'
with open(input, 'r') as f:
    data = [section.splitlines() for section in f.read().split("\n\n")]

section_1, section_2 = data

page_ordering_rules = defaultdict(list)
for line in section_1:
    left, right = map(int, (i for i in line.split("|")))
    page_ordering_rules[left].append(right)


# def is_in_right_order(pages):
#     for p in pages:
#         idx = pages.index(p)
#         left = pages[:idx]
#         right = pages[idx+1:]
#         while left:
#             check = left.pop(0)
#             if p not in page_ordering_rules[check]:
#                 return False
#         while right:
#             check = right.pop(0)
#             if check not in page_ordering_rules[p]:
#                 return False
#     return True


# correctly_ordered_updates = []
# incorrectly_ordered_updates = []
# for line in section_2:
#     pages = list(map(int, (i for i in line.split(","))))
#     if is_in_right_order(pages):
#         correctly_ordered_updates.append(pages)
#     else:
#         incorrectly_ordered_updates.append(pages)

# print(f"puzzle 1: {sum(c[len(c)//2] for c in correctly_ordered_updates)}")


# print(incorrectly_ordered_updates)
# corrected_updates = []

# for iou in incorrectly_ordered_updates:
#     corrected_update = []
#     numbers = set(iou)
#     while numbers:
#         for num in numbers:
#             print(num, numbers, corrected_update)
#             if all(num2 in page_ordering_rules[num] for num2 in numbers if num2 != num):
#                 corrected_update.append(num)
#                 numbers.remove(num)
#                 break
#     corrected_updates.append(corrected_update)


# print(f"incorrectly_ordered_updates {len(incorrectly_ordered_updates)}")
# print(f"corrected_updates {len(corrected_updates)}")
# print(f"puzzle 2: {sum(c[len(c)//2] for c in corrected_updates)}")


p1, p2 = open('day5.txt').read().split('\n\n')
updates = [list(map(int, line.split(','))) for line in p2.splitlines()]

orders = defaultdict(list)
for order in p1.splitlines():
    before, after = order.split('|')
    orders[int(before)].append(int(after))

part1 = 0
part2 = 0
for pages in section_2:
    sorted_pages = sorted(pages, key=lambda page: -
                          len([order for order in orders[page] if order in pages]))
    if pages == sorted_pages:
        part1 += pages[len(pages) // 2]
    else:
        part2 += sorted_pages[len(sorted_pages) // 2]
print('Part 1', part1)
print('Part 2', part2)
