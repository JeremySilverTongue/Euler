

limit = 100

max_digit_sum = 0
for a in xrange(1, limit):
    for b in xrange(1, limit):
        digit_sum = sum(map(int, str(a ** b)))
        if digit_sum > max_digit_sum:
            # print a ** b, digit_sum
            max_digit_sum = digit_sum

print max_digit_sum
