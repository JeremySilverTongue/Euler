# import numpy as np
# import fractions


# n = 100000000



# def summarum(phi, num, denom):
#     s = 0
#     limit = fractions.Fraction(num, denom)
#     phi[1] = 1
#     min_frac = 10
#     i = 2
#     while i < n:
#         # print i
#         if phi[i] == 0:
#             phi[i] = i - 1

#             j = 2

#             while j * i < n:
#                 if phi[j] != 0:
#                     q = j
#                     f = i - 1

#                     while q % i == 0:
#                         f *= i
#                         q //= i

#                     phi[i * j] = f * phi[q]
#                 j += 1
#         s += phi[i]
#         i += 1

#         # print "derp"
#         # print phi[i], i


#         resiliant_fraction = fractions.Fraction(phi[i], i-1)
#         if resiliant_fraction == 0:
#             resiliant_fraction = 10
#         if resiliant_fraction < min_frac:
#             min_frac = resiliant_fraction
#         if i % 1000 == 0:
#             print i, float(min_frac), float(limit)
#         # print i, resiliant_fraction, limit
#         if resiliant_fraction != 0 and resiliant_fraction < limit:
#             print i, float(resiliant_fraction), float(limit)
#             return i


# # print summarum(np.zeros(n+1, np.int32),4,10)
# print summarum(np.zeros(n+1, np.int32), 15499, 94744)


# test = [2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720, 1441440, 4324320, 21621600, 367567200, 6983776800, 13967553600, 321253732800, 2248776129600, 65214507758400, 195643523275200, 6064949221531200]
import numbthy
# for x in test:
#     print x, float(numbthy.eulerphi(x))/(x-1), float(15499)/ 94744 ,\
#     float(numbthy.eulerphi(x))/(x-1)< float(15499)/ 94744

# ratio = 10
# for x in xrange(2,10000):
#     new_ratio = float(numbthy.eulerphi(x))/(x-1)
#     if new_ratio < ratio:
#         ratio = new_ratio
#         print x,","


primorial = [2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230, 200560490130, 7420738134810, 304250263527210, 13082761331670030, 614889782588491410, 32589158477190044730, 1922760350154212639070]

def increasing_phi(limit = 1000):
    x = 0
    y = 1
    counter = 0
    pri = primorial[x]
    next_pri = primorial[x+1]
    while counter < limit:
        counter += 1
        if pri * y < next_pri:
            y += 1
            yield pri * y
        else:
            x += 1
            y = 1
            pri = primorial[x]
            next_pri = primorial[x+1]

for x in increasing_phi():
    print x#, float(numbthy.eulerphi(x))/(x-1), float(15499)/ 94744 ,\
    #float(numbthy.eulerphi(x))/(x-1)< float(15499)/ 94744 






