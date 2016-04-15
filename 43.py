

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


def test_substring_divisibility(array, elements, denominator):
    sub_string = int("".join([str(array[x]) for x in elements]))
    # print sub_string, denominator, sub_string %denominator

    return sub_string % denominator == 0


def full_test(array):
    if not test_substring_divisibility(array, (7, 8, 9), 17):
        return False
    if not test_substring_divisibility(array, (1, 2, 3), 2):
        return False
    if not test_substring_divisibility(array, (2, 3, 4), 3):
        return False
    if not test_substring_divisibility(array, (3, 4, 5), 5):
        return False
    if not test_substring_divisibility(array, (4, 5, 6), 7):
        return False
    if not test_substring_divisibility(array, (5, 6, 7), 11):
        return False
    if not test_substring_divisibility(array, (6, 7, 8), 13):
        return False

    return True
    # return all([
    # test_substring_divisibility(array, (1,2,3), 2),
    # test_substring_divisibility(array, (2,3,4), 3),
    # test_substring_divisibility(array, (3,4,5), 5),
    # test_substring_divisibility(array, (4,5,6), 7),
    # test_substring_divisibility(array, (5,6,7), 11),
    # test_substring_divisibility(array, (6,7,8), 13),
    # test_substring_divisibility(array, (7,8,9), 17)
    # ])


# test_num = [1,4,0,6,3,5,7,2,8,9]
# test_num2 = [1,4,0,6,3,5,7,2,9,8]


# # print test_substring_divisibility(test_num, (7,8,9), 17)
# print full_test(test_num)
# print full_test(test_num2)

numbers = []

counter = 0
for p in permute([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]):
    counter += 1
    if full_test(p):
        numbers.append(int("".join(map(str, p))))
    # if counter > 1000000:
    #     break


print numbers
print sum(numbers)
