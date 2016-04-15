import numbthy


max_ratio = 0
max_n = 0
limit = 1000000
for x in range(1, limit):
    ratio = float(x) / numbthy.eulerphi(x)
    if ratio > max_ratio:
        print x, ratio
        max_ratio = ratio
        max_n = x

print max_ratio, max_n
