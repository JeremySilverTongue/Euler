

def sum_of_square_digits(n):
    return sum(map(lambda x: int(x) * int(x), str(n)))

ends = {1: 1, 89: 89}


def end_of_chain(n):
    if n not in ends:
        new_n = sum_of_square_digits(n)
        ends[n] = end_of_chain(new_n)
    return ends[n]


def count_89_ends(limit=10000000):
    total = 0
    for x in xrange(1, limit):
        if x % (limit / 100) == 0:
            print x, total

        if end_of_chain(x) == 89:
            total += 1
    return total

# print sum_of_square_digits()
# for x in range
# print end_of_chain(85)
print count_89_ends()
# print ends
