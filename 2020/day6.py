'''
    Advent of Code Day 6
    https://adventofcode.com/2020/day/6
'''

# input from website in raw format
with open('day6.input.txt', 'r') as f:
    data = f.read().splitlines()
# shall be stored in a list
my_puzzle = []

# an empty lines signals the end of a data block
while data.count("")>0:
    y = data.index("")
    my_puzzle.append(data[0:y])
    data = data[y+1:]
# we have one more data set than empty lines
my_puzzle.append(data)
# now we have all the data in a nice list format

# just checking if everything is in the list
for i in range(0, len(my_puzzle)):
    print(my_puzzle[i])

# Puzzle #1
sum_of_counts_anyone_answered_yes = 0
for i in range(0, len(my_puzzle)):
    s = set()
    for element in my_puzzle[i]:
        for letter in element:
            s.add(letter)
    sum_of_counts_anyone_answered_yes += len(s)
print(f"sum_of_counts_anyone_answered_yes: {sum_of_counts_anyone_answered_yes}")

# Puzzle #2
sum_of_counts_everyone_answered_yes = 0
for i in range(0, len(my_puzzle)):
    tmp_list = my_puzzle[i][0]
    for j in range(1, len(my_puzzle[i])):
        tmp_list = [x for x in my_puzzle[i][j] if x in tmp_list]
    sum_of_counts_everyone_answered_yes += len(tmp_list)
print(f"sum_of_counts_everyone_answered_yes: {sum_of_counts_everyone_answered_yes}")