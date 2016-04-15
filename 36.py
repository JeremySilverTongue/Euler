def digits(n):
    return map(int, str(n))


def check_palindrome(n):
    if isinstance(n, list):
        return list(n) == list(reversed(n))
    if isinstance(n, str):
        return n == str(reversed(n))
    elif isinstance(n, int):
        return check_palindrome(digits(n))
    else:
        print type(n)


def my_bin(n):
    return list(bin(n)[2:])


def check_dual_base(n):
    return check_palindrome(n) and check_palindrome(my_bin(n))


def find_dual_base(limit):
    palindromes = []
    for x in range(limit):
        if check_dual_base(x):
            palindromes.append(x)
    return palindromes


# print find_dual_base(1000000)

print sum([0, 1, 3, 5, 7, 9, 33, 99, 313, 585, 717, 7447, 9009, 15351, 32223, 39993, 53235, 53835, 73737, 585585])
