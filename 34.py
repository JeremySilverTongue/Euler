import math


def digits(n):
    return map(int, str(n))


def check_factorial(n):
    return n == sum(map(math.factorial, digits(n)))


def find(limit=1000000):
    found = []
    for x in range(3, limit):
        if check_factorial(x):
            found.append(x)
    return found

found = find()
print found
print sum(found)
