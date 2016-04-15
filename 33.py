

def is_curious_fraction(numerator, denominator):
    num_str = str(numerator)
    denom_str = str(denominator)
    if len(num_str) == 2 and len(denom_str) == 2:
        # print "Passed length check"
        num_first_digit, num_second_digit = str(numerator)
        denom_first_digit, denom_second_digit = str(denominator)
        if denom_second_digit != '0' and num_first_digit != num_second_digit:
            # print passed
            if float(numerator) / denominator < 1:
                if float(num_second_digit) / float(denom_first_digit) == float(numerator) / denominator and num_first_digit == denom_second_digit:
                    return True
                if float(num_first_digit) / float(denom_second_digit) == float(numerator) / denominator and num_second_digit == denom_first_digit:
                    return True
    return False


def find_curious_fractions(limit=100):
    fractions = []
    for x in range(limit):
        for y in range(limit):
            if is_curious_fraction(x, y):
                fractions.append((x, y))
    return fractions


def divides(num, denom):
    # print "Does", num, "divide", denom, num % denom == 0
    return num % denom == 0


def reduce_fraction(num, denom):
    new_num = num
    new_denom = denom
    for x in range(num, 2, -1):
        if divides(new_num, x) and divides(new_denom, x):
            new_num = new_num / x
            new_denom = new_denom / x
    return new_num, new_denom


def multiply_fractions(frac_list):
    out_num, out_denom = 1, 1
    for frac in frac_list:
        out_num *= frac[0]
        out_denom *= frac[1]
    return reduce_fraction(out_num, out_denom)

# print is_curious_fraction(49,98)
curious = find_curious_fractions()
print multiply_fractions(curious)

print reduce_fraction(2, 4)
