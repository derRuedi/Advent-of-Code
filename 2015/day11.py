'''
    Advent of Code 2015
    https://adventofcode.com/2015/
'''

import pathlib
from time import sleep
import helper

# input from website in raw format
data = "vzbxkghb"


def increment_password(password):
    if set(password) == {'z'}:
        return ["a"]*8

    if password[-1] != "z":
        password[-1] = chr(ord(password[-1]) + 1)
    else:
        return increment_password(password[:-1]) + ['a']

    return password


def contains_increasing_straight(password):
    # include increasing straight of at least three letters, like "abc", "bcd", "cde", and so on, up to "xyz"
    includes_increasing_straight = False
    for i in range(len(password)-3+1):
        includes_increasing_straight = ord(password[i]) == ord(
            password[i+1]) - 1 and ord(password[i+1]) == ord(password[i+2]) - 1
        if includes_increasing_straight:
            break

    if not includes_increasing_straight:
        # print(f"Password '{password}' does not include increasing straight.")
        return False

    return True


def contains_confusing_letters(password):
    # no "i", "o" or "l" in password
    if any(item in password for item in ["i", "o", "l"]):
        # print(f"Password '{password}' includes confusing letter(s) 'i', 'o' or 'l'.")
        return True
    return False


def contains_overlapping_pairs_of_letters(password, amount=2):
    # must contain at least two different, non-overlapping pairs of letters, like "aa", "bb", or "zz"
    letter_pairs = set()
    for i in range(len(password)-2+1):
        if password[i] == password[i+1]:
            letter_pairs.add(password[i])
    if len(letter_pairs) < amount:
        # print(f"Password '{password}' must contain at least {amount} different, non-overlapping pairs of letters, like 'aa', 'bb', or 'zz'")
        return False
    return True


def password_requirements_met(password):
    requirements = []

    requirements.append(contains_increasing_straight(password))
    requirements.append(not contains_confusing_letters(password))
    requirements.append(contains_overlapping_pairs_of_letters(password))

    return all(requirements)


def find_next_password(password):
    print(f"The next password after {password} is: ", end="")
    password = list(password)
    password = increment_password(password)
    while not password_requirements_met(password):
        password = increment_password(password)
    print("".join(password))
    return "".join(password)


password = data
password = find_next_password(password)
password = find_next_password(password)
