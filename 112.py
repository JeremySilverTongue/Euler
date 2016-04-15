def is_bouncy(number):
    digits = list(str(number))
    # print digits
    # print sorted(digits)
    # print
    # print digits
    return digits != sorted(digits) and list(reversed(digits)) != sorted(digits)


def find_n_for_bouncy_fraction(fraction=.5):
    num_bouncy = 0
    n = 1
    while float(num_bouncy) / n < fraction:
        n += 1
        if is_bouncy(n):
            # print n, "is_bouncy"
            num_bouncy += 1
    return n

print find_n_for_bouncy_fraction(.99)

# print is_bouncy(134468)
# print is_bouncy(1)
# print is_bouncy(10)
# print is_bouncy(155349)
