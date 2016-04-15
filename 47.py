import numbthy


def distinct_factors(n):
    factors = numbthy.factor(n)
    # print factors
    return len(factors)


for x in range(1, 1000000):
    if distinct_factors(x) == 4 and\
            distinct_factors(x + 1) == 4 and\
            distinct_factors(x + 2) == 4 and\
            distinct_factors(x + 3) == 4:
        print x
