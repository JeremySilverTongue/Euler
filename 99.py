import math# total = 1000

# for x in range(total):
# 	print x, total-x, float(x)/(total-x), x ** (total-x)

with open("p099_base_exp.txt") as numbers:
	line_number = 0
	data= []
	for row in numbers:
		line_number += 1
		base, exponant = map(int,row.split(","))
		data.append((line_number, base, exponant))
	# data = [map(int,row.split(",")) for row in numbers]


biggest = 0
biggest_line = 0
for line_number, base, exponant in data:
	if exponant * math.log(base) > biggest:
		biggest = exponant * math.log(base)
		biggest_line = line_number

print biggest_line

# print data

# base1, exponant1 = 519432,525806
# base2, exponant2 = 632382,518061


# print exponant1 * math.log(base1)
# print exponant2 * math.log(base2)
# print len(str(base1 ** exponant1))