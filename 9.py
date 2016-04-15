import math


def find_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = math.sqrt(a * a + b * b)
            if c == int(c) and a + b + c == 1000:
                return a * b * c


print find_triplet()
