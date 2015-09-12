def power_series(limit):
	return sum([x ** x for x in range(1,limit+1)])


print power_series(1000)