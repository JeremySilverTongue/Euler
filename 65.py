import fractions


def continued_fraction(denominators):
    convergent = denominators[-1]
    for denom in reversed(denominators[:-1]):
        convergent = denom + fractions.Fraction(1, convergent)
        print convergent, float(convergent)
    return convergent


def get_e_denoms(limit=100):
    denoms = [2]
    for x in xrange(1, limit):
        if x % 3 == 2:
            denoms.append((x / 3 + 1) * 2)
        else:
            denoms.append(1)
    return denoms

# continued_fraction([1,2,2])
denoms = get_e_denoms()

print continued_fraction(denoms)

print sum(map(int, str(6963524437876961749120273824619538346438023188214475670667)))
