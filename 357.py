# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.

# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.

import numbthy
import sympy

def divisors(n):   
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_prime_generator(n):
	return n if all([sympy.isprime(d + n/d) for d in divisors(n)]) else 0

counter = 0
limit = 100000000
index = 1
n = 1
while n < limit:
	n = sympy.prime(index) -1
	index += 1
	counter += is_prime_generator(n)



print counter
