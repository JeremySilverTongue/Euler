

# def digit_of_power_of_two(position, exponant):


# for x in range(10,100):
# print "".join(list(reversed(str(2 ** x))))


def truncated_exponentiation(base, exponant, limit, multiple=1, offset=0):
    product = 1
    for exp in range(exponant):
        product *= base
        digits = str(product)
        if len(digits) > limit:
            product = int(digits[-limit:])
            # print product
    product *= multiple
    product += offset
    digits = str(product)
    if len(digits) > limit:
        product = int(digits[-limit:])
    return product


# print truncated_exponentiation(2, 10, 10, 1, 0)

print truncated_exponentiation(2, 7830457, 10, 28433, 1)
