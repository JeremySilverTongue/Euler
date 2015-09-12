
FILE_NAME = "p082_matrix.txt"

def load_data(file_name = FILE_NAME):
	with open(file_name) as data_file:
		return [map(int,line.split(",")) for line in data_file]


# LAST_UP = 1
# LAST_DOWN = 2
# LAST_RIGHT = 3

# path_memo = {}

# def min_path(y, x,grid, last = 0):
# 	key = (y,x)
# 	if key not in path_memo:
# 		height = len(grid)
# 		width = len(grid[0])
# 		if x == width-1:
# 			path_memo[key] = grid[y][x]
# 		else:
# 			possibilities = []
# 			possibilities.append(min_path(y,x+1, grid, LAST_RIGHT))
# 			if not last == LAST_DOWN and y != 0:
# 				possibilities.append(min_path(y-1,x, grid, LAST_UP))
# 			if not last == LAST_UP and y != height -1:
# 				possibilities.append(min_path(y+1,x, grid, LAST_DOWN))
# 			path_memo[key] = grid[y][x] + min(possibilities)
# 	return path_memo[key]



# # grid = [[1,1,1],[2,0,2],[5,0,0]]

# # grid = load_data()

grid = [
	[131, 673, 234, 103,  18],
	[201,  96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524,  37, 331]
	]

# grid = [
# 	[100,0,0,0,0],
# 	[0,0,0,100,150]
# 	]

# print min([min_path(y,0,grid) for y in range(len(grid))])
# # print min([min_path(y,0,grid) for y in range(len(grid))])
# # print min_path(1,3,grid)

# # print min_path(0,0,grid)
# print path_memo

# def in_grid(height, width, x, y):
# 	"""
# 	Used to figure out if a new cell we might want to visit
# 	is still in the grid
# 	"""
# 	return (0 <= x < width) and (0 <= y < height)


class Queue:
	def __init__(self, starting_dictionary = None):
		if starting_dictionary is None:
			self.dict = {}
		else:
			self.dict = starting_dictionary

	def add(self, key, value):
		if key not in self.dict or self.dict[key] > value:
			self.dict[key] = value

	def isNotEmpty(self):
		return True if self.dict else False

	def pop(self):
		if self.isNotEmpty():
			key = min(self.dict.keys())
			return key, self.dict.pop(key)

queue = Queue()
print queue.isNotEmpty()
queue.add((1,2), 3)
print queue.isNotEmpty()
(x,y),cost =  queue.pop()
print x, y, cost
print queue.isNotEmpty()



def add_node(grid, visited, frontier, cost_so_far, y, x):
	height = len(grid)
	width = len(grid[0])
	if (0 <= x < width) and (0 <= y < height):
		new_cost = cost_so_far + grid[y][x]
		key = (y, x)
		if key not in visited or visited[key] > new_cost:
			frontier.append((new_cost, y, x))
			# print "Adding {} to frontier".format(key)
			visited[new_cost] = key

# def search(grid):
# 	height = len(grid)
# 	width = len(grid[0])
# 	visited = dict([((y, 0), grid[y][0]) for y in range(height)])
# 	# print visited
# 	frontier = [(grid[y][0],y, 0) for y in range(height)] 
# 	sucessful_path_scores = []
# 	counter = 0
# 	while frontier:
# 		cost_so_far, y, x = min(frontier)
# 		frontier.remove((cost_so_far, y, x))
# 		if x == width-1:
# 			return cost_so_far
# 		counter += 1
# 		if counter % 1000 == 0:
# 			print len(frontier)
# 		# Add move right
# 		add_node(grid, visited,frontier, cost_so_far, y    , x + 1)
# 		add_node(grid, visited,frontier, cost_so_far, y-1    , x )
# 		# add_node(grid, visited,frontier, cost_so_far, y+1    , x )
# 		# print "finished expanding",  y, x				
# 	# print "Didn't find it? That shouldn't happen..."
# 	# print visited
# 	# print frontier



# grid = load_data()
# print search(grid)