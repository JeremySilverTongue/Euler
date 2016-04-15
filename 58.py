import sympy


diagonal_numbers = 1
primes = 0
last = 1
for layer in range(1, 100000):
    for x in range(4):
        last += 2 * layer
        diagonal_numbers += 1
        if sympy.isprime(last):
            primes += 1
    if float(primes) / diagonal_numbers < .1:
        print 2 * layer + 1, primes, diagonal_numbers, float(primes) / diagonal_numbers
        break
