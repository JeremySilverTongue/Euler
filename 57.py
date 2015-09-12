from fractions import Fraction

# def continued_fraction(denominators):
# 	convergent = denominators[-1]
# 	for denom in reversed(denominators[:-1]):
# 		convergent =  denom + fractions.Fraction(1,convergent)
# 		# print convergent
# 	return convergent



# denoms = [1,2]
# counter = 0

# for x in range(1,1000):
# 	convergent = continued_fraction(denoms)
# 	if len(str(convergent.numerator)) > len(str(convergent.denominator)):
# 		counter += 1
# 		print convergent
# 	denoms.append(2)

# print continued_fraction([1, 2,2,2,2]).numerator

def count(limit = 1000):
	convergent = 0
	counter = 0
	for x in range(limit):
		convergent =Fraction(1, 2 + convergent)
		out = convergent +1
		if len(str(out.numerator)) > len(str(out.denominator)):
			counter += 1
			print out
	return counter


print count()