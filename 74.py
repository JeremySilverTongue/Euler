from math import factorial



counter = 0

for x in range(1,1000000 +1):
	fact = x
	chain = []
	while fact not in chain:
		chain.append(fact)
		fact = sum(map(lambda x: factorial(int(x)), str(fact)))
	# print x, len(chain), chain
	if len(chain) == 60:
		counter += 1

print counter


# chain_memo = {}

# def chain_length(n):
# 	if n not in chain_memo:
		