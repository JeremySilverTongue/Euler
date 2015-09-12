def factors(n):   
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def sum_of_factors(n):
	if n == 0:
		return 0

	return sum(factors(n))-n

def test_amicable(n):
	return sum_of_factors(sum_of_factors(n)) == n and sum_of_factors(n) != n

def find_amicable(limit):
	amicable = []
	for x in range(1,limit):
		# print x
		if test_amicable(x):
			amicable.append(x)
	return amicable


print sum(find_amicable(10000))


# print factors(1)
# print sum_of_factors(1)
# print test_amicable(1)