'''
    Advent of Code Day 17
    https://adventofcode.com/2020/day/17
'''

# input from website in raw format

#		# # . . . . # .
#		# . # . . # . .
#		. . . # . . . .
#		. . . # . # . .
#		# # # . . . . #
#		# . # . . . . #
#		. # . . . . # #
#		. # . # # # . #

data = []
with open('day17.input.txt', 'r') as f:
    data = f.read().splitlines()

sample_data = [
	".#.",
	"..#",
	"###"
]

def create_cube(size):
	cube = [[[ "." for x in range(size) ] for y in range (size) ] for z in range(size) ]
	return cube

def create_tesseract(size):
	tesseract = [[[[ "." for x in range(size) ] for y in range (size) ] for z in range(size) ] for w in range(size) ]
	return tesseract

def create_cube_from_input(input):
	z = len(input)//2
	size = len(input)
	cube = create_cube(size)
	for y, line in enumerate(input):
		for x, letter in enumerate(line):
			# the cube list containts the coordinates in the following form: cube[Z][Y][X]
			cube[z][y][x] = letter
	return cube

def create_tesseract_from_input(input):
	z = len(input)//2
	w = len(input)//2
	size = len(input)
	tesseract = create_tesseract(size)
	for z, plane in enumerate(input):
		for y, line in enumerate(plane):
			for x, letter in enumerate(line):
				# the tesseract list containts the coordinates in the following form: tesseract[W][Z][Y][X]
				tesseract[w][z][y][x] = letter
	return tesseract


def print_3d_cube(cube):
	print(f"Printing cube\n{cube}.", end="\n\n")
	for layer in cube:
		for row in layer:
			print(row)
		print() # blank line for easier readability
	print("-"*80, end="\n\n")


def count_cube_point_active_neighbors(cube, point):
	count = 0

	# the 26 checkpoints/directions in a 3d space surrounding a single point
	checkpoints = []
	for x in range(-1,2,1):
		for y in range(-1,2,1):
			for z in range(-1,2,1):
				if (x == 0 and y == 0 and z == 0):
					continue
				checkpoints.append( [x, y, z] )

	for checkpoint in checkpoints:
		check_x = point[0] + checkpoint[0]
		check_y = point[1] + checkpoint[1]
		check_z = point[2] + checkpoint[2]
		size = len(cube)
		# no need to check if out of bounds
		if check_x < 0 or check_y < 0 or check_z < 0 or check_x >= size or check_y >= size or check_z >= size:
			continue
		# the cube list containts the coordinates in the following form: cube[Z][Y][X]
		if cube[check_z][check_y][check_x] == "#":
			count += 1

	return count


def count_tesseract_point_active_neighbors(tesseract, point):
	count = 0

	# the 80 checkpoints/directions in a 3d space surrounding a single point
	checkpoints = []
	for x in range(-1,2,1):
		for y in range(-1,2,1):
			for z in range(-1,2,1):
				for w in range(-1,2,1):
					if (x == 0 and y == 0 and z == 0 and w == 0):
						continue
					checkpoints.append( [x, y, z, w] )

	for checkpoint in checkpoints:
		check_x = point[0] + checkpoint[0]
		check_y = point[1] + checkpoint[1]
		check_z = point[2] + checkpoint[2]
		check_w = point[3] + checkpoint[3]
		size = len(tesseract)
		# no need to check if out of bounds
		if check_x < 0 or check_y < 0 or check_z < 0 or check_w < 0 or check_x >= size or check_y >= size or check_z >= size or check_w >= size:
			continue
		# the cube list containts the coordinates in the following form: tesseract[W][Z][Y][X]
		if tesseract[check_w][check_z][check_y][check_x] == "#":
			count += 1

	return count


def create_points_in_cube(cube):
	cube_size = range(0, len(cube))
	points = []

	for z in cube_size:
		for y in cube_size:
			for x in cube_size:
				points.append( [x, y, z] )
	return points


def create_points_in_tesseract(tesseract):
	tesseract_size = range(0, len(tesseract))
	points = []

	for w in tesseract_size:
		for z in tesseract_size:
			for y in tesseract_size:
				for x in tesseract_size:
					points.append( [x, y, z, w] )
	return points


def increase_cube(cube):
	for layer in cube:
		for row in layer:
			row.insert(0, ".")
			row.append(".")
		
		layer.insert(0, ["."] * len(layer[0]))
		layer.append(["."] * len(layer[0]))
	cube.insert(0, [["."] * len(layer[0]) ] * len(layer[0]))
	cube.append([["."] * len(layer[0]) ] * len(layer[0]))

def increase_tesseract(tesseract):
	for cube in tesseract:
		for layer in cube:
			for row in layer:
				row.insert(0, ".")
				row.append(".")
			
			layer.insert(0, ["."] * len(layer[0]))
			layer.append(["."] * len(layer[0]))
		cube.insert(0, [["."] * len(layer[0]) ] * len(layer[0]))
		cube.append([["."] * len(layer[0]) ] * len(layer[0]))
	tesseract.insert(0, [[["."] * len(layer[0]) ] * len(layer[0]) ] * len(layer[0]))
	tesseract.append([[["."] * len(layer[0]) ] * len(layer[0]) ] * len(layer[0]))


def is_cube_point_active(cube, point):
	# the cube list containts the coordinates in the following form: cube[Z][Y][X]
	if cube[point[2]][point[1]][point[0]] == "#":
		return True
	else:
		return False


def is_tesseract_point_active(tesseract, point):
	# the tesseract list containts the coordinates in the following form: tesseract[W][Z][Y][X]
	if tesseract[point[3]][point[2]][point[1]][point[0]] == "#":
		return True
	else:
		return False


def update_cube_point(cube, point, value):
	cube[point[2]][point[1]][point[0]] = value


def update_tesseract_point(tesseract, point, value):
	tesseract[point[3]][point[2]][point[1]][point[0]] = value


def execute_cube_cycle(cube):
	new_cube = create_cube(len(cube))
	points = create_points_in_cube(cube)

	for point in points:
		active_neighbors = count_cube_point_active_neighbors(cube, point)
		if is_cube_point_active(cube, point):
			if active_neighbors == 2 or active_neighbors == 3:
				# print(f"{point} has {active_neighbors} active_neighbors - stays active")
				update_cube_point(new_cube, point, "#")
			else:
				# print(f"{point} has {active_neighbors} active_neighbors - gets inactive")
				update_cube_point(new_cube, point, ".")
		else:
			if active_neighbors == 3:
				# print(f"{point} has {active_neighbors} active_neighbors - gets active")
				update_cube_point(new_cube, point, "#")
			# else:
				# print(f"{point} has {active_neighbors} active_neighbors - nothing happens")

	return new_cube


def execute_tesseract_cycle(tesseract):
	new_tesseract = create_tesseract(len(tesseract))
	points = create_points_in_tesseract(tesseract)

	for point in points:
		active_neighbors = count_tesseract_point_active_neighbors(tesseract, point)
		if is_tesseract_point_active(tesseract, point):
			if active_neighbors == 2 or active_neighbors == 3:
				# print(f"{point} has {active_neighbors} active_neighbors - stays active")
				update_tesseract_point(new_tesseract, point, "#")
			else:
				# print(f"{point} has {active_neighbors} active_neighbors - gets inactive")
				update_tesseract_point(new_tesseract, point, ".")
		else:
			if active_neighbors == 3:
				# print(f"{point} has {active_neighbors} active_neighbors - gets active")
				update_tesseract_point(new_tesseract, point, "#")
			# else:
				# print(f"{point} has {active_neighbors} active_neighbors - nothing happens")

	return new_tesseract


def count_active_cube_points(cube):
	count = 0
	points = create_points_in_cube(cube)

	for point in points:
		if is_cube_point_active(cube, point):
			count += 1
	return count


def count_active_tesseract_points(tesseract):
	count = 0
	points = create_points_in_tesseract(tesseract)

	for point in points:
		if is_tesseract_point_active(tesseract, point):
			count += 1
	return count


def boot_cube(input):
	my_cube = create_cube_from_input(input)

	# it takes six cycles to boot
	for i in range(0,6):
		increase_cube(my_cube)
		my_cube = execute_cube_cycle(my_cube)
	
	return count_active_cube_points(my_cube)

def boot_tesseract(input):
	my_tesseract = create_tesseract_from_input(input)

	# it takes six cycles to boot
	for i in range(0,6):
		increase_tesseract(my_tesseract)
		my_tesseract = execute_tesseract_cycle(my_tesseract)

	return count_active_tesseract_points(my_tesseract)


print(f"The answer to puzzle #1's sample data is: {boot_cube(sample_data)}")
print(f"The answer to puzzle #1's data is: {boot_cube(data)}")

print(f"The answer to puzzle #2's sample data is: {boot_tesseract(sample_data)}")
print(f"The answer to puzzle #2's data is: {boot_tesseract(data)}")












# just some code to create the checkpoints programmatically

# checkpoints = [
#     [-1,-1,+1], [ 0,-1,+1], [+1,-1,+1], [-1, 0,+1], [+1, 0,+1], [-1,+1,+1], [ 0,+1,+1], [+1,+1,+1], [ 0, 0,+1], [-1,-1, 0], [ 0,-1, 0], [+1,-1, 0], [-1, 0, 0], [+1, 0, 0], [-1,+1, 0], [ 0,+1, 0], [+1,+1, 0], [-1,-1,-1], [ 0,-1,-1], [+1,-1,-1], [-1, 0,-1], [+1, 0,-1], [-1,+1,-1], [ 0,+1,-1], [+1,+1,-1], [ 0, 0,-1]
# ]


# my_2d_points = []
# for x in range(-1,2,1):
#     for y in range(-1,2,1):
#         if (x == 0 and y == 0):
#                 continue
#         my_2d_points.append( [x, y] )

# print(my_2d_points)
# print(len(my_2d_points))


# my_3d_points = []
# for x in range(-1,2,1):
#     for y in range(-1,2,1):
#         for z in range(-1,2,1):
#             if (x == 0 and y == 0 and z == 0):
#                 continue
#             my_3d_points.append( [x, y, z] )

# print(my_3d_points)
# print(len(my_3d_points))


# my_4d_points = []
# for x in range(-1,2,1):
#     for y in range(-1,2,1):
#         for z in range(-1,2,1):
#             for w in range(-1,2,1):
#                 if (x == 0 and y == 0 and z == 0 and w == 0):
#                     continue
#                 my_4d_points.append( [x, y, z, w] )

# print(my_4d_points)
# print(len(my_4d_points))