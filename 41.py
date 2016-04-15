import sympy


def is_pandigital(n):
    return sorted(str(n)) == [str(i) for i in xrange(1, len(str(n)) + 1)]


limit = 100000000
for i in xrange(1, 100000000):
    prime = sympy.prime(i)
    if i % (limit / 100) == 0:
        print "Checked", i, "of", limit
    if is_pandigital(prime):
        print prime
