def digits(n):
	return map(int,str(n))


def check_sum_of_fifth_powers(n):
	if n == 1:
		return False
	return n == sum([digit ** 5 for digit in digits(n)])

def find_such_numbers(limit = 1000000):
	found = []
	for n in range(1,limit):
		if check_sum_of_fifth_powers(n):
			found.append(n)
	return found

# print find_such_numbers()

print sum([4150, 4151, 54748, 92727, 93084, 194979])