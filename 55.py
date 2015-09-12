

def is_palindrome(num):
	return list(str(num)) == list(reversed(str(num)))

def reverse_and_add(num):
	return num + int("".join(list(reversed(str(num)))))


lychrel_counter = 0
for x in xrange(10000):
	y = reverse_and_add(x)
	counter = 1
	while not is_palindrome(y) and counter < 50:
		y = reverse_and_add(y)
		counter += 1
	if counter == 50:
		lychrel_counter += 1

print lychrel_counter

