# If we list all the natural numbers below 10 that are multiples of 3 or
# 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(factors, limit):
    accumulator = [0 for i in range(0, limit)]
    for factor in factors:
        multiple = 0
        while multiple < limit:
            accumulator[multiple] = multiple
            multiple += factor
    return sum(accumulator)


print sum_of_multiples([3, 5], 10)
print sum_of_multiples([3, 5], 1000)
