

def num_digits(n):
    return len(str(n))

counter = 0
for exponant in range(100):
    base = 1
    power = base ** exponant
    while len(str(power)) <= exponant:
        if len(str(power)) == exponant:
            print power
            counter += 1
        base += 1
        power = base ** exponant

print counter
