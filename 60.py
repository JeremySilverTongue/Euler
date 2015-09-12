import sympy
from itertools import permutations


def check_all_concats(primes, membership_set):
	for p1 in primes:
		for p2 in primes:
			if p1 != p2:
				if p1+p2 not in membership_set:
					# print p1+p2, "Isn't prime"
					return False
				if p2+p1 not in membership_set:
					return False
					# print p2+p1, "Isn't prime"
	# return primes, "works"

	return True



perm_set = []

primes = [str(sympy.prime(x)) for x in range(1, 10000)]
# print primes
primes_set = set([str(sympy.prime(x)) for x in range(1, 10000000)])

print "Starting search"

for x in primes:
	new_sets = []
	for perm in perm_set:
		test_set = perm + [x]
		if check_all_concats(test_set, primes_set):
			new_sets.append(test_set)
			if len(test_set) == 5:
				print test_set
				print sum(map(int,test_set))
	perm_set += new_sets
	perm_set.append([x])


# print sorted(perm_set,key = lambda x : len(x))

# def find_primes_set(size):
# 	for prime in 
# 	if size ==







# for test in permutations(primes_set, 4):
# 	print test
	# if check_all_concats(test, primes_set):
	# 	print "Found it:", test
