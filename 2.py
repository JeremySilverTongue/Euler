import unittest


# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

fib_memo = {1: 1, 2: 2}


def fib(n):
    if n < 1:
        return -1
    if n not in fib_memo:
        fib_memo[n] = fib(n - 1) + fib(n - 2)
    return fib_memo[n]


def sum_of_even_fib(limit):
    total = 0
    n = 1
    next_term = fib(n)
    while next_term < limit:
        if next_term % 2 == 0:
            total += next_term
        n += 1
        next_term = fib(n)
    return total

print sum_of_even_fib(4e6)


class TestFibFunctions(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fib(1), 1)

    def test_2(self):
        self.assertEqual(fib(2), 2)

if __name__ == '__main__':
    unittest.main()
