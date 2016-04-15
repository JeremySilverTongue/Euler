

sums = {(1, 1): 1}

hits = 0
misses = 0


def number_of_sums(n, max_allowed=None):

    global hits, misses

    if max_allowed == None:
        max_allowed = n - 1
    key = (n, max_allowed)
    if key not in sums:
        misses += 1
        if max_allowed == 1:
            sums[key] = 1
        elif n == 0:
            sums[key] = 1
        else:
            total = 0
            for x in range(min([max_allowed, n]), 0, -1):
                # print "Sub problem of finding the ways to write {} using only
                # up to {}".format(n-x, x)
                total += number_of_sums(n - x, x)
            sums[key] = total
    else:
        hits += 1
    return sums[key]


# print number_of_sums(4,2)

# for x in range(1,101):
    # print "There are {} ways to sum to {}".format(number_of_sums(x),x)

print number_of_sums(100)

print "There were {} hits and {} misses for a hit rate of {}".format(hits, misses, float(hits) / (misses + hits))
# # print number_of_sums(1)
# # print number_of_sums(2)
# # print number_of_sums(6)
# print sums

# n = 5 - 2
# n = 3 -2
# print n*(n+1)/2
