def is_last_permutation(items):
	return items == list(reversed(sorted(items)))




def next_permutation(items):
	if is_last_permutation(items):
		print "No more permutations"
		return sorted(items)

	head = items[0]
	rest = items[1:]
	if is_last_permutation(rest):
		ordered = sorted(items)
		head = ordered[ordered.index(head)+1]
		rest = [item for item in ordered if item != head]
	else:
		rest = next_permutation(rest)
	return [head] + rest

def n_th_permutation(items, n):
	current = items
	for i in range(1,n):
		if i % (n/100) == 0:
			print i, current
		# print current
		current = next_permutation(current)

	return current




	# if len(items) = 1:
		# return None



# 	return [max(items)] + sort(items.re)


# print is_last_permutation([])
# print next_permutation([1,2,3])
print n_th_permutation([0,1,2,3,4,5,6,7,8,9],1000000)
# print n_th_permutation([0,1,2],2)


#2783915460