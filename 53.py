from math import factorial as fac


def binomial(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom


big_binoms = []
for x in xrange(1, 101):
    for y in xrange(x):
        binom = binomial(x, y)
        if binom > 1000000:
            big_binoms.append(binom)

print len(big_binoms)
