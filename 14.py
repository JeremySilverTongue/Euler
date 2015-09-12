
def collatz_length(n):
	length = 0
	state = n
	while state > 1:
		# print length, state
		length += 1
		if state % 2 == 0:
			state /= 2
		else:
			state = 3 * state +1
	return length


def longest_chain(limit):
	longest_length = 0
	longest_start = -1
	for start in range(limit):
		if start % (limit/100) == 0:
			print start, longest_length
		length = collatz_length(start)
		if length > longest_length:
			longest_length = length
			longest_start = start
	return longest_start, longest_length

# collatz_length(5)
# for x in range(10):
# 	print collatz_length(x)

print longest_chain(1000000)