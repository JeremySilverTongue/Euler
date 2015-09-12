def spiral_sum(size):
	total = 1
	head = 1
	for x in range(1,size,2):
		for y in range(4):
			head += x +1
			total += head
	return total



print spiral_sum(1001)