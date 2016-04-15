from collections import defaultdict

limit = 10000


def generate(func, minimum=1000, limit=10000):
    index = 1
    last_result = func(index)
    result = []
    while last_result < limit:
        if last_result >= minimum:
            result.append(last_result)
        index += 1
        last_result = func(index)
    return map(str, result)

triangle = generate(lambda n: n * (n + 1) / 2)
square = generate(lambda n: n * n)
pentagonal = generate(lambda n: n * (3 * n - 1) / 2)
hexagonal = generate(lambda n: n * (2 * n - 1))
heptagonal = generate(lambda n: n * (5 * n - 3) / 2)
octagonal = generate(lambda n: n * (3 * n - 2))

# print triangle
# print square
# print pentagonal
# print hexagonal
# print heptagonal
# print octagonal


# , hexagonal, heptagonal, octagonal]
figurate_numbers = [triangle, square, pentagonal]


def to_lookup(numbers):
    lookup = defaultdict(list)
    for number in numbers:
        lookup[number[:2]].append(number)
    return lookup

figurate_lookups = [to_lookup(entry) for entry in figurate_numbers]

print figurate_lookups


# def rotations(string):
# 	working = string
# 	out = [string]
# 	for x in range(len(string)-1):
# 		working = working[-1] + working[:-1]
# 		out.append(working)
# 	return out

# print rotations("1234")


# def find_rotations(candidates):
# for number in candidates[0]:


def find_rotation(input_number, candidates, future_candidates):
    for candidate in candidates:
        if in


# for pent in pentagonal:
# 	rot = rotations(pent)


# 	for catagory in figurate_numbers:
# 		for

# triangles = []
# n =
# while

 # [n*(n+1)/2 for n in range(1,100)]
