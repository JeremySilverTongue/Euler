import sys
import math
limit = 10000



pentagonal_numbers = [n*(3*n - 1) /2 for n in xrange(1,limit)]
pentagonal_numbers_set = set(pentagonal_numbers)

# print pentagonal_numbers

min_difference = sys.maxsize
for x in pentagonal_numbers:
	for y in pentagonal_numbers:
		if (x + y in pentagonal_numbers_set) and (x - y in pentagonal_numbers_set) and math.abs(x-y) < min_difference:
			print "Found one", (x,y)
			min_difference = abs(x-y)

print min_difference
