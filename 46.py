import sympy

limit = 10000
primes = set([sympy.prime(n) for n in xrange(1,limit)])
double_squares = [2*n*n for n in xrange(1,limit)]
odd_composites = [n for n in range(3,limit,2) if n not in primes]

# print primes
# print double_squares
# print odd_composites


# for odd in odd_composites:
# 	found = False
# 	for p in filter(lambda x: x < odd, primes):
# 		if odd - p in double_squares:
# 			found = True
# 	if not found:
# 		print "Found one!", p


def search(targets, fast_growing_list, remainder_set):
	for target in targets:
		found = False
		# print "target", target
		for x in fast_growing_list:
			# print "testing", x
			if x > target:
				# print x, target
				break
			if target - x in remainder_set:
				found = True
				break
		if not found:
			return target




print search(odd_composites, double_squares, primes)
