import sympy


def consecutive_primes(a, b):
    n = 0
    while sympy.isprime(n * n + a * n + b):
        n += 1
    return n


def find_max_consecutive_primes(limit):
    max_primes = 0
    max_a, max_b = 0, 0
    for a in range(-limit, limit + 1):
        for b in range(-limit, limit + 1):
            primes = consecutive_primes(a, b)
            if primes > max_primes:
                max_primes = primes
                max_a, max_b = a, b
    return max_primes, max_a, max_b, max_a * max_b

# print consecutive_primes(1,41)
print find_max_consecutive_primes(1000)
