import sympy
import collections

#print sympy.isprime(10)

def digits(n):
	return map(int,str(n))

def digits_to_int(numList):
    s = ''.join(map(str, numList))
    return int(s)

def check_trucations(n):

	number_digits = digits(n)

	for x in range(1,len(number_digits)):
		truncation1 = number_digits[x:]
		truncation2 = number_digits[:len(number_digits)- x]
		number1 = digits_to_int(truncation1)
		number2 = digits_to_int(truncation2)

		if (not sympy.isprime(number1)) or (not sympy.isprime(number2)):
			return False
	return True


def find_tuncatable_primes(limit=100000):
	primes = []
	for x in range(5,limit):
		prime = sympy.prime(x)
		if check_trucations(prime):
			primes.append(prime)
	return primes

# print check_trucations(123456)


# print prime(100)
print sum(find_tuncatable_primes())