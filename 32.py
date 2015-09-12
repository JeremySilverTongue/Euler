# import numbthy


#def check_pandigital_product(factor1, factor2)

def is_pandigital(number):
	return sorted(str(number)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def has_pandigital_identity(x):
	for y in range(1,x):
		if x % y == 0:
			if is_pandigital(str(x)+str(y)+str(x/y)):
				return True
	return False


def find_unusual_numbers(limit= 1000000):
	unusual = []
	for x in range(1, limit):
		if x % (limit/100) == 0:
			print "Checked", x, "found", len(unusual), "sum", sum(unusual)

		if has_pandigital_identity(x):
			unusual.append(x)
	return unusual



# print is_pandigital("987654321")
# print list("123456789")
# print has_pandigital_identity(724)
unusual = find_unusual_numbers()
print unusual
print sum(unusual)