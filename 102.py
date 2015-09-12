import math
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Point:

	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

# def mid_point(point1, point2):
	# return Point(x = float(point1.x + point2.x)/2, y = point1.y + point2.y)

def dot(point1, point2):
	return point1.x * point2.x + point1.y * point2.y

# def distance(point1, point2):
# 	diff = Point(point1.x - point2.x, point1.y - point2.y)
# 	return math.sqrt(diff.x*diff.x + diff.y * diff.y)

# origin = Point(0,0)

# def check_triangle(point1, point2, point3):
# 	print distance(point1, origin), distance(point1, point3)
# 	print distance(point2, origin), distance(point2, point3)
# 	test1 = distance(point1, origin) < distance(point1, point3)
# 	test2 = distance(point2, origin) < distance(point2, point3)
# 	return test1 and test2



def check_point_in_triangle(A, B, C, P):
	v0 = C - A
	v1 = B - A
	v2 = P - A

	dot00 = dot(v0, v0)
	dot01 = dot(v0, v1)
	dot02 = dot(v0, v2)
	dot11 = dot(v1, v1)
	dot12 = dot(v1, v2)

	invDenom = 1.0 / (dot00 * dot11 - dot01 * dot01)
	u = (dot11 * dot02 - dot01 * dot12) * invDenom
	v = (dot00 * dot12 - dot01 * dot02) * invDenom

	return (u >= 0) and (v >= 0) and (u + v < 1)

def check_origin_in_triangle(A,B,C):
	return check_point_in_triangle(A, B, C, Point(0,0))


FILE_NAME = "p102_triangles.txt"
count = 0
with open(FILE_NAME) as triangles_file:
	for line in triangles_file:
		x1,y1,x2,y2,x3,y3 = line.strip().split(',')
		if check_origin_in_triangle(Point(x1,y1), Point(x2,y2), Point(x3,y3)):
			count += 1

print count
