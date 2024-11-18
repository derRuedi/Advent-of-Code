'''
    Advent of Code 2016
    https://adventofcode.com/2016/
'''

import hashlib


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# input from website in raw format
secret_key = "ugkcyxxp"


password = ""
i = -1

while len(password) < 8:
    i += 1
    hash_value = f"{secret_key}{i}"
    hash_result = hashlib.md5(hash_value.encode('utf-8')).hexdigest()
    if hash_result[0:5] == "00000":
        password += hash_result[5]
print(password)

print()

password = list("________")
i = -1
animation = ["/", "-", "\\"]

while password.count("_") != 0:
    i += 1
    hash_value = f"{secret_key}{i}"
    hash_result = hashlib.md5(hash_value.encode('utf-8')).hexdigest()
    if hash_result[0:5] == "00000":
        if hash_result[5] in (str(c) for c in range(8)) and password[int(hash_result[5])] == "_":
            password[int(hash_result[5])] = hash_result[6]
    if i % 1234 == 0:
        print("Password: ", end="")
        for char in password:
            if char == '_':
                print(bcolors.FAIL + animation[0] + bcolors.ENDC, end='')
            else:
                print(bcolors.OKGREEN + bcolors.BOLD +
                      char + bcolors.ENDC, end='')
        print("\t Hash: " + hash_result, end="")
        print("\t Hashes: " + str(i), end="")
        print('\r', end='')
        animation.append(animation.pop(0))
print("Password: " + bcolors.OKGREEN +
      bcolors.BOLD + "".join(password) + bcolors.ENDC)
