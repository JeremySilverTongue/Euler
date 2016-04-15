def generate_concated_numbers(limit):
    return "".join([str(x) for x in range(limit)])


d = generate_concated_numbers(1000000)

print int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])
