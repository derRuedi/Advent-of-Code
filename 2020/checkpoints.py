checkpoints = [
    [-1,-1,+1], [ 0,-1,+1], [+1,-1,+1], [-1, 0,+1], [+1, 0,+1], [-1,+1,+1], [ 0,+1,+1], [+1,+1,+1], [ 0, 0,+1], [-1,-1, 0], [ 0,-1, 0], [+1,-1, 0], [-1, 0, 0], [+1, 0, 0], [-1,+1, 0], [ 0,+1, 0], [+1,+1, 0], [-1,-1,-1], [ 0,-1,-1], [+1,-1,-1], [-1, 0,-1], [+1, 0,-1], [-1,+1,-1], [ 0,+1,-1], [+1,+1,-1], [ 0, 0,-1]
]


my_2d_points = []
for x in range(-1,2,1):
    for y in range(-1,2,1):
        if (x == 0 and y == 0):
                continue
        my_2d_points.append( [x, y] )

print(my_2d_points)
print(len(my_2d_points))


my_3d_points = []
for x in range(-1,2,1):
    for y in range(-1,2,1):
        for z in range(-1,2,1):
            if (x == 0 and y == 0 and z == 0):
                continue
            my_3d_points.append( [x, y, z] )

print(my_3d_points)
print(len(my_3d_points))


my_4d_points = []
for x in range(-1,2,1):
    for y in range(-1,2,1):
        for z in range(-1,2,1):
            for w in range(-1,2,1):
                if (x == 0 and y == 0 and z == 0 and w == 0):
                    continue
                my_4d_points.append( [x, y, z, w] )

print(my_4d_points)
print(len(my_4d_points))