from random import randint

dictionary = {}

dictionary["entry1"] = "value1"


def print_dictionary(dictionary):
    for k, v in dictionary.items():
        print(k, v)


def manipulate_dictionary(dictionary, entry, value):
    dictionary[entry + str(randint(0, 10))] = value + str(randint(10, 20))
    if len(dictionary) < 5:
        manipulate_dictionary(dictionary, entry +
                              str(randint(0, 10)), value + str(randint(0, 10)))


print_dictionary(dictionary)
print("---")

manipulate_dictionary(dictionary, "quark", "wups")


print_dictionary(dictionary)
print("---")
