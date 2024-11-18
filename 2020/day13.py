'''
    Advent of Code Day 13
    https://adventofcode.com/2020/day/13
'''

# input from website in raw format
data = []
with open('day13.input.txt', 'r') as f:
    data = f.read().splitlines()


sample_data = [
    "939",
    "7,13,x,x,59,x,31,19"
]

# data = sample_data


# Puzzle #1
timestamp = int(data[0])
bus_lines = [ int(x) for x in data[1].split(",") if x != "x"]
bus_lines_with_x = [ x for x in data[1].split(",") ]

bus_lines_wait_time = { int(x):((timestamp // int(x) + 1) * int(x) - timestamp) for x in data[1].split(",") if x != "x" }

best_bus = min(bus_lines_wait_time, key=bus_lines_wait_time.get)
wait_time_for_best_bus = best_bus * bus_lines_wait_time.get(best_bus)

print(f"The answer to puzzle #1 is: {wait_time_for_best_bus}.")


# Puzzle #2 - works for small data sets... computaionally intense

#timestamp = 0
#bus_lines_and_offset = { bus_lines[i]: bus_lines_with_x.index(str(bus_lines[i])) for i in range(0, len(bus_lines)) }
#
#while True:
#	
#	found_timestamp = True
#	
#	for bus, offset in bus_lines_and_offset.items():
#		if (timestamp + offset) % bus != 0:
#			found_timestamp = False
#			break
#			
#	if found_timestamp:
#		break
#	
#	timestamp += 1
#	
#	if timestamp % 1000000 == 0:
#		print(timestamp)
#
#print(f"The answer to puzzle #2 is: {timestamp}.")


bus_lines_and_offset = [ (int(bus_lines_with_x[i]), i) for i,j in enumerate(bus_lines_with_x) if j != "x" ]

timestamp = 0
step = 1

for bus, offset in bus_lines_and_offset:
	while (timestamp + offset) % bus != 0:
		timestamp += step
	step *= bus
		
print(f"The answer to puzzle #2 is: {timestamp}.")
