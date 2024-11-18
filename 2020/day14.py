'''
    Advent of Code Day 14
    https://adventofcode.com/2020/day/14
'''

# input from website in raw format
data = []
with open('day14.input.txt', 'r') as f:
    data = f.read().splitlines()

sample_data = [
	"mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
	"mem[8] = 11",
	"mem[7] = 101",
	"mem[8] = 0"
]

sample_data2 = [
	"mask = 000000000000000000000000000000X1001X",
	"mem[42] = 100",
	"mask = 00000000000000000000000000000000X0XX",
	"mem[26] = 1"
]
   
import re

# Puzzle #1
def decoder_version1(data):
	match_mem = re.compile("[0-9]+")
	mask = 0
	
	my_mem = {}
	
	for line in data:
		line = line.replace(" ", "")
		left, right = line.split("=")
		
		if line.startswith("mask"):
			mask = right
			# print(f"mask: {mask}")
		else:
			address = int(match_mem.search(left).group(0))
			# value should be a 36 bit unsigned integer in base 2 
			value = f"{int(right):036b}"
			
			# then, value should be masked with the bitmask and written to the memory position
			my_mem[address] = "".join([ n if n != "X" else value[idx] for idx, n in enumerate(mask) ])
			# print(f"mem: {memory} contains {value}")
	
	return sum(int(value, 2) for mem, value in my_mem.items())
	

# Puzzle #2
def decoder_version2(data):
	match_mem = re.compile("[0-9]+")
	mask = 0
	
	my_mem = {}
	
	for line in data:
		line = line.replace(" ", "")
		left, right = line.split("=")
		
		if line.startswith("mask"):
			mask = right
			# print(f"mask:\n{mask}", end="\n\n")
		else:
			value = int(right)
			# get the address as unsigned 36-bit integer in base 2
			address = f"{int(match_mem.search(left).group(0)):036b}"
			
			# apply the bit mask
			address = "".join([ address[idx] if n == "0" else n if n == "1" else "X" for idx, n in enumerate(mask) ])
			
			# now deal with the floating bits
			# how many X do we have to deal with
			num_of_x = address.count("X")
			
			# that makes 2^num_of_x possible combinations; create...
			combinations = [ f"{x:0{num_of_x}b}" for x in list(reversed(range(2 ** num_of_x)))]
			
			# ... and apply them
			for combination in combinations:
				tmp_address = address
				for i in range(num_of_x):
					tmp_address = tmp_address.replace('X', combination[i], 1)
				
				# and add every single combinations address:value pair to my memory
				my_mem[tmp_address] = value
	
	# then sum up all values in my memory and return
	return sum( value for mem, value in my_mem.items())

print(f"The answer to puzzle #1's sample data is {decoder_version1(sample_data)}.")
print(f"The answer to puzzle #1 is {decoder_version1(data)}.", end="\n\n")

print(f"The answer to puzzle #2's sample data is {decoder_version2(sample_data2)}.")
print(f"The answer to puzzle #2 is {decoder_version2(data)}.")
