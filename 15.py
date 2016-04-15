
# def outgoing

path_count = {(0, 0): 0, (1, 1): 2}


def lattice_paths(height, width):
    key = (height, width)
    if key not in path_count:
        if height == 0 or width == 0:
            count = 1
        else:
            count = lattice_paths(height - 1, width) + \
                lattice_paths(height, width - 1)
        path_count[key] = count
    return path_count[key]

# def lattice_paths(size):
# 	if size < 1:
# 		return 0
# 	if size == 1:
# 		return 2
# 	return 2*(size-1 + lattice_paths(size-1))


# for x in range(20):
    # print lattice_paths(x)

print lattice_paths(20, 20)
