import sympy
import collections

#print sympy.isprime(10)

def digits(n):
	return map(int,str(n))



def rotations(n):
	number_digits = collections.deque(digits(n))
	rots = []
	for x in range(len(number_digits)):
		number_digits.rotate()
		rots.append(int("".join(map(str,list(number_digits)))))
	return rots

def check_circular_prime(n):
	return all(map(sympy.isprime,rotations(n)))

def find_circular_primtes(limit=100):
	palindromes = []
	for x in range(limit):
		if check_circular_prime(x):
			palindromes.append(x)
	return palindromes


# print rotations(123234567876545678)

# print int("".join(map(str,[8, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7])))
# print int("".join([8, 1, 2, 3, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 5, 6, 7]))

primes = find_circular_primtes(1000000)
print primes
print len(primes)