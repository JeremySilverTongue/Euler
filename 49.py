from collections import Counter


import sympy




# index = 1
# prime = 2


# primes_of_interest = [sympy.prime(x) for x in range(169,1230)]
# # primes_of_interest = [sympy.prime(x) for x in range(169,180)]

# prime_sets = map(lambda x: Counter(str(x)), primes_of_interest)

# zipped_primes = zip(prime_sets,primes_of_interest)

# triples = []
# for prime in primes_of_interest:
# 	matches = filter(lambda x: x[0] == Counter(str(prime)), zipped_primes)
# 	if len(matches) ==3:
# 		triple = tuple([x[1] for x in matches])
# 		if triple not in triples:
# 			triples.append(triple) 

# print triples
# triples = [(1021, 1201, 2011), (1033, 1303, 3301), (1051, 5011, 5101), (1063, 3061, 6301), (1181, 1811, 8111), (1223, 2213, 3221), (1229, 2129, 9221), (1259, 2591, 9521), (1433, 3413, 4133), (1471, 1741, 7411), (1489, 8419, 8941), (1619, 6911, 9161), (1663, 6163, 6361), (1777, 7177, 7717), (1801, 8011, 8101), (2053, 2503, 5023), (2069, 2609, 6029), (2141, 2411, 4211), (2239, 2293, 3229), (2441, 4241, 4421), (2459, 2549, 4259), (2543, 4253, 4523), (2633, 3623, 6323), (2677, 2767, 6277), (2707, 7027, 7207), (2749, 4297, 4729), (2857, 5827, 8527), (3253, 5233, 5323), (3373, 3733, 7333), (3389, 8933, 9833), (3583, 3853, 8353), (3863, 6833, 8363), (4057, 4507, 5407), (4099, 4909, 9049), (4261, 4621, 6421), (4691, 6491, 9461), (4789, 4987, 7489), (4969, 6949, 9649), (5039, 5309, 5903), (5077, 7057, 7507), (5081, 5801, 8501), (5399, 5939, 9539), (5477, 7457, 7547), (5563, 5653, 6553), (5669, 6569, 6659), (6089, 8069, 8609), (6679, 6967, 7669), (6689, 6869, 8669), (7687, 7867, 8677), (8191, 9181, 9811), (9091, 9109, 9901)]

# for triple in triples:
# 	diff1 = triple[2] - triple[1]
# 	diff2 =  triple[1] - triple[0]
# 	print diff1 == diff2, diff1, diff2, triple






# print prime_sets

# def contains_three_permutations(n, collection):


# for x in :


# 	print x, sympy.prime(x)




primes_of_interest = [sympy.prime(x) for x in range(169,1230)]


def is_permutation(n1, n2):
	return Counter(str(n1)) == Counter(str(n2))

for prime in primes_of_interest:
	for second_prime in primes_of_interest:
		if second_prime <= prime:
			continue
		if is_permutation(prime, second_prime):
			third_prime = 2*second_prime - prime
			if third_prime in primes_of_interest:
				if is_permutation(third_prime, second_prime):
					print prime, second_prime, third_prime





