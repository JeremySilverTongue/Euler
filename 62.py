

cubes = set()

cube = 0
index = 0
limit = 100000000000000
while cube < limit:
    index += 1
    cube = index * index * index
    cubes.add(cube)

sorted_cubes = [sorted(str(cube)) for cube in cubes]

for cube in sorted(cubes):
    sorted_digits = sorted(str(cube))
    match_count = 0
    for comparison_cube in sorted_cubes:
        if comparison_cube == sorted_digits:
            match_count += 1
    # print cube, match_count
    if match_count == 5:
        print "Found it: ", cube
        break
