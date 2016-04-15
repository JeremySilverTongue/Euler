import sys

FILE_NAME = "p081_matrix.txt"


def load_data(file_name=FILE_NAME):
    with open(file_name) as data_file:
        return [map(int, line.split(",")) for line in data_file]


def min_path_cost(data, x=0, y=0, memo=None):
    if memo is None:
        memo = {}
    key = (x, y)
    x_dim = len(data[0])
    y_dim = len(data)
    if key not in memo:
        if x == x_dim - 1 and y == y_dim - 1:
            memo[key] = data[y][x]
        elif x >= x_dim or y >= x_dim:
            memo[key] = sys.maxsize
        else:
            go_down_value = min_path_cost(data, x, y + 1, memo)
            go_right_value = min_path_cost(data, x + 1, y, memo)
            current = data[y][x]
            memo[key] = current + min([go_right_value, go_down_value])
    return memo[key]


# 	if key not in path_count:
# 		if height == 0 or width == 0:
# 			count = 1
# 		else:
# 			count = lattice_paths(height-1, width) + lattice_paths(height, width-1)
# 		path_count[key] = count
# 	return path_count[key]

# def

# print data[0]


data = load_data()
print min_path_cost(data)
