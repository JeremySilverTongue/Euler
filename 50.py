import sympy
from collections import defaultdict

#.isprime(


sum_of_primes = defaultdict(int)

def consecutive_primes_length(n):
	if n not in sum_of_primes:
		starting_prime_index = 1
		starting_prime = sympy.prime(starting_prime_index)
		while starting_prime <= n:
			total = starting_prime
			# print "Starting at", starting_prime
			run_length = 1

			while total <= n:
				# print "\tTrying run length", run_length
				if sympy.isprime(total):
					sum_of_primes[total] = max([run_length, sum_of_primes[total]])
					# print "\t", total, "Is the sum of", run_length, "primes"
				run_length += 1
				total += sympy.prime(starting_prime_index + run_length-1)
				

			starting_prime_index += 1
			starting_prime = sympy.prime(starting_prime_index)




	return sum_of_primes[n]



consecutive_primes_length(1000000)
# print sum_of_primes
print max(sum_of_primes.items(), key = lambda item: item[1])
