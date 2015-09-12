

def division(num, denom):
	new_num = num
	depth = 0
	repeat = False
	fixed = ''
	repeated = []
	divisions = []
	while not repeat:
		while new_num < denom:
			new_num *= 10
			fixed += ''
			


def unit_fraction_cycle_length(denom):
	if denom < 2:
		return
	num = 10
	numerators = [0]
	safety = 0
	while num not in numerators and safety < 10000:
		safety += 1
		# print num, numerators
		numerators.append(num)
		while num < denom:
			num *= 10
			# numerators.append(0)

		(_, num) = divmod(num, denom)
		if num ==0:
			return 0
	return len(numerators) - numerators.index(num)

for x in range(2,10):
	print x, unit_fraction_cycle_length(x)


print max([(unit_fraction_cycle_length(x), x) for x in range(2,1000)])
# print unit_fraction_cycle_length(7)
# print unit_fraction_cycle_length(4)
# print unit_fraction_cycle_length(5)
# print unit_fraction_cycle_length(6)
# print unit_fraction_cycle_length(7)

