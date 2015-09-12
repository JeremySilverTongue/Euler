import math
import collections

limit = 3000
triangular = [n*(n+1)/2 for n in xrange(limit)]

# x, y, area, count, interval

Result = collections.namedtuple('Result',['x','y', 'area', 'count', 'interval'])
closest = Result(0,0, 0, 0, 10000000)

target = 2000000
for x in xrange(limit):
	for y in xrange(limit):
		count = triangular[x] * triangular[y]
		interval = abs(count - target)
		if interval < closest.interval:
			closest = Result(x, y, x *y, count, interval)

print closest


# print triangular