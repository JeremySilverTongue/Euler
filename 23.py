def proper_factors(n):
    factors = set(reduce(list.__add__, ([i, n // i]
                                        for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    factors.remove(n)
    return list(factors)


def check_abundant(n):
    if n == 0:
        return False
    return (sum(proper_factors(n)) > n)


def find_abundant(limit):
    abundant = []
    for x in range(limit):
        if check_abundant(x):
            abundant.append(x)
    return abundant


def can_find_sum(n, summators):
    for sum1 in summators:
        if n - sum1 in summators:
            # print sum1,"+",n - sum1,"=", n
            return True
    # print "Can't sum to", n
    return False


def find_sum_of_unsummable(limit, summators):
    sum_of_unsummable = 0
    for x in range(limit):
        if x % (limit / 100) == 0:
            print x, sum_of_unsummable
        if not can_find_sum(x, summators):
            sum_of_unsummable += x
    return sum_of_unsummable


# print proper_factors(10)
# print check_abundant(12)
limit = 30000
abundant = set(find_abundant(limit))
# print len(abundant)
# print abundant[:100]
# print can_find_sum( 10000, abundant)
print find_sum_of_unsummable(limit, abundant)
