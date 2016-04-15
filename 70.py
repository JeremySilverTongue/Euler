from numbthy import eulerphi


def are_permutations(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


limit = 10000000

ratio = 100
winning_n = 0

for n in xrange(2, limit):
    phi = eulerphi(n)
    if are_permutations(n, phi) and float(n) / phi < ratio:
        print n, phi
        winning_n = n
        ratio = float(n) / phi


print winning_n, ratio

# print sorted(str(54321))
