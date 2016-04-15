import math
import re

pattern = re.compile("1.2.3.4.5.6.7.8.9.0")


def is_match(num):
    return bool(pattern.match(str(num)))

print is_match(1929304050607080900)
print is_match(192930405060708090)


progress = 0
for x in xrange(1000000000, 1400000000, 10):
    progress += 1
    if progress % 100000 == 0:
        print "Progress update", progress
    if is_match(x * x):
        print "Found it!", x


# 1000000000
# 1010101010
# 1388993898
# 1400000000

# def is_match(num):
# 	return bool(re.match("1.2.3",str(num)))

# print is_match(1929304050607080900)
# print is_match(192930405060708090)


# progress = 0
# for x in xrange(1000000000, 1400000000):
# 	if x % (1400000000.-1000000000)/100 == 0:
# 		progress +=1
# 		print "Progress update", progress
# 	if is_match(x*x):
# 		print "Found it!", x
