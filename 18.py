
import collections
import functools


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


raw_data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# mini_raw_data = """3
# 7 4
# 2 4 6
# 8 5 9 3"""

mini_raw_data = """75
95 64
17 47 82
18 35 87 10"""

with open('p067_triangle.txt') as raw_data_file:
    big_raw_data = raw_data_file.read()


def parse_raw_data(raw_data):
    lines = raw_data.split("\n")
    data = []
    for line in lines:
        data.append(map(int, line.split()))
    return data


def cost_of_leftmost_path(data, row, column):
    return sum([data[row_index][column] for row_index in range(row, len(data))])


def cost_of_rightmost_path(data, row, column):
    return sum([data[row + offset][column + offset] for offset in range(len(data) - row)])


test_data = parse_raw_data(raw_data)
mini_data = parse_raw_data(mini_raw_data)
big_data = parse_raw_data(big_raw_data)[:-1]
# print big_data
data = big_data
path_memo = {}


def simple_find_path(row, column):

    if (row, column) not in path_memo:
        cost = data[row][column]
        if row < len(data) - 1:
            right_subtree = simple_find_path(row + 1, column + 1)
            left_subtree = simple_find_path(row + 1, column)
            cost += max([right_subtree, left_subtree])
        path_memo[(row, column)] = cost
    return path_memo[(row, column)]


# print mini_data
print simple_find_path(0, 0)
# print find_path(test_data, 0, 0)

# print cost_of_leftmost_path(mini_data,0,0)
# print cost_of_rightmost_path(mini_data,0,0)
# print cost_of_leftmost_path(data,0,0)
# print cost_of_rightmost_path(data,0,0)


# def find_path(data,row,column):
#     # print "Finding cost of subtree rooted at {row}, {column}".format(row=row, column=column)
#     cost = data[row][column]
#     # print row, len(data), row <len(data)
#     if row < len(data) -1:
#         left_choice = data[row+1][column]
#         right_choice = data[row+1][column+1]

# print "at", cost,"left_choice", left_choice, "right_choice",
# right_choice

#         # print "recursive case"
#         right_path = cost_of_rightmost_path(data,row, column)
#         left_path = cost_of_leftmost_path(data,row, column)

#         if (left_choice > right_choice and left_path >= right_path) or left_path > right_path:
#             print "going left to", left_choice
#             cost += find_path(data, row+1, column)
#         else:
#             print "going right to", right_choice
#             cost += find_path(data, row+1, column+1)


#         # if cost_of_left_path > cost_of_right_subtree:
#         #     cost += cost_of_left_path
#         #     print "going left"
#         # else:
#         #     cost += cost_of_right_subtree
#         #     print "going right"

#         # cost += max([cost_of_left_path, cost_of_right_subtree])

#         # print cost_of_right_subtree
#         # print cost_of_left_path
#     return cost
