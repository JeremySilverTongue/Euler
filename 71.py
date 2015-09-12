from fractions import Fraction
from math import ceil, floor

# print float(Fraction(3,7) * 1000000)


unordered = set()


limit = 1000000
# denominators = []
# for d in range(limit,0,-1):
# 	print map(lambda x: x % d ==0, denominators)
# 	if not any(map(lambda x: x % d ==0, denominators)):
# 		print "Adding", d
# 		denominators.append(d)

# print d
target = Fraction(3,7)
plus_minus = 1

for d in range(2,limit+1):
	unordered.add(Fraction(int(floor(d * target)),d))

	# closest = int(d * target)
	# low = closest - plus_minus
	# high = closest + plus_minus
	# for n in range(low,high+1):
	# 	unordered.add(Fraction(n,d))

# print ceil(.5)
# print sorted([Fraction(int(ceil(d * target)),d) for d in range(2,limit+1)])

print "Built"
ordered= sorted(unordered)
print "Sorted"
index = ordered.index(target)
print ordered[index-1]
print float(ordered[index-1]), float(target)