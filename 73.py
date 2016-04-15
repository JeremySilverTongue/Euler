from fractions import Fraction, gcd
from math import ceil, floor


unordered = set()

limit = 12000

min_value = Fraction(1, 3)
max_value = Fraction(1, 2)
counter = 0


def mfloor(input):
    if input == floor(input):
        return int(input - 1)
    else:
        return int(floor(input))


def mceil(input):
    if input == ceil(input):
        return int(input + 1)
    else:
        return int(ceil(input))


for d in range(2, limit + 1):
    # print d * min_value
    # print d * max_value
    min_num = mceil(d * min_value)
    max_num = mfloor(d * max_value)
    # print d, min_num, max_num, max_num - min_num +1

    for i in range(min_num, max_num + 1):
        if gcd(i, d) == 1:
            counter += 1
            # unordered.add(Fraction(i,d))
    # if max_num >= min_num:
        # counter += max_num - min_num +1
    # unordered.add(Fraction(int(floor(d * target)),d))

    # closest = int(d * target)
    # low = closest - plus_minus
    # high = closest + plus_minus
    # for n in range(low,high+1):
    # 	unordered.add(Fraction(n,d))

# print ceil(.5)
# print sorted([Fraction(int(ceil(d * target)),d) for d in range(2,limit+1)])
print counter

print "Built"
# ordered= sorted(unordered)
# print ordered
# print map(float, ordered)
# print "Sorted"
# index = ordered.index(target)
# print ordered[index-1]
# print float(ordered[index-1]), float(target)
