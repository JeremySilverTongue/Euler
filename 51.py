from sympy import prime, isprime


limit = 100000
primes = [str(prime(x)) for x in range(1,limit)]
prime_set = set(primes)

for p in primes:
	for char in p:
		count = 0
		for replacement in map(str,range(10)):
			if p.replace(char, replacement) in prime_set:
				count += 1
		if count == 8:
			print p



# print primes


# print "1234".replace("1","4")