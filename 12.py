def triangular_number(n):
    return n * (n + 1) / 2


def number_of_divisors(n):
    # count = 0
    # for x in range(1,n/2):
    # 	if n % x == 0:
    # 		count +=1
    return len(factors(n))


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def search(divisors_to_find):
    triangular = 1
    n = 1
    while number_of_divisors(triangular) < divisors_to_find:
        if n % 100 == 0:
            print number_of_divisors(triangular)
        n += 1
        triangular = triangular_number(n)

    return n, triangular


# for x in range(10):
# 	print number_of_divisors(x)

print search(500)
