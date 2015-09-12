
def generate_triangular(limit):
	return [n * (n + 1) / 2 for n in xrange(limit)]

def generate_pentagonal(limit):
	return [n * (3 * n - 1) / 2 for n in xrange(limit)]

def generate_hexagonal(limit):
	return [n * (2*n - 1) for n in xrange(limit)]



def find_magic(limit = 100000):
	tri = generate_triangular(limit)
	pent = set(generate_pentagonal(limit))
	hexagonal = set(generate_hexagonal(limit))
	for t in tri:
		if t in pent and t in hexagonal:
			print t


print find_magic()