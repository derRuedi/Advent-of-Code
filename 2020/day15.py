'''
    Advent of Code Day 15
    https://adventofcode.com/2020/day/15
'''

# input from website
data = [ 0,1,5,10,3,12,19 ]

sample_data = [ 0, 3, 6 ]

# Puzzle #1
def memory_game(data, turn):
	nums_spoken = [ x for x in data ]
		
	for turn in range(len(data)+1, turn+1):
		last_number_spoken = nums_spoken[-1]
		
		if last_number_spoken in nums_spoken and nums_spoken.count(last_number_spoken) > 1:
			speak = nums_spoken[::-1][1:].index(last_number_spoken) + 1
		else:
			speak = 0
			
		nums_spoken.append(speak)

	return speak

# Puzzle #2
def memory_game2(data, until_turn):
	nums_spoken_in_turn = { num : idx+1 for idx, num in enumerate(data[:-1]) } # {0: 1, 3: 2} for sample data
	next_number = data[-1]
	
	for turn in range(len(data)+1, until_turn+1):
		last_turn = turn - 1
		
		if next_number in nums_spoken_in_turn:
			speak = last_turn - nums_spoken_in_turn[next_number]
			# print(f"speak = {speak} = {last_turn} - {nums_spoken_in_turn[next_number]}")
		else:
			speak = 0
		
		nums_spoken_in_turn[next_number] = last_turn
		next_number = speak

	return speak

	

# print(f"The answer to Puzzle #1's sample data is: {memory_game(sample_data, 2020)}")
print(f"The answer to Puzzle #1 is: {memory_game(data, 2020)}")

# print(f"The answer to Puzzle #2's sample data is: {memory_game2(sample_data, 30000000)}")
print(f"The answer to Puzzle #2 is: {memory_game2(data, 30000000)}")