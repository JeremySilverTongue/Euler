def sum_square_difference(limit):
	sum_of_squares = 0
	for x in range(1,limit+1):
		sum_of_squares += x*x
	straight_sum = sum(range(1,limit+1))
	square_of_sum = straight_sum * straight_sum
	return square_of_sum - sum_of_squares


print sum_square_difference(10)
print sum_square_difference(100)