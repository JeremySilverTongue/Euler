# from collections import Counter


# # REFERENCE_COUNT = Counter("123456789")
# DIGITS = "123456789"

# def find_pandigital_product(mult):
# 	# product = Counter()
# 	products = ""
# 	n = 1
# 	while n < 9:
# 		products = products + str(mult * n)
# 		# print products
# 		if sorted(products) == sorted(DIGITS):
# 			print mult, "is pandigital with n=", n
# 			# print product
# 			for x in range(1,n+1):
# 				print mult, "x", x, "=", mult*x
# 		n += 1


# count = Counter("1234")
# print count
# count.update("567")
# print count

# for x in range(100000):
# for x in range(0,10000):
# find_pandigital_product(x)


def problem38():
    largest = int()
    intex = 0
    for i in xrange(9000, 10000):
        temp = str(i) + str(i * 2)
        if "0" not in temp:
            if len(set(temp)) == 9:
                if int(temp) > largest:
                    largest = int(temp)
                    index = i

    return index, largest

print problem38()
