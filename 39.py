import math

def check_integer_tri(p, o, a):
    h = math.sqrt(o*o + a*a)
    return h == int(h) and p == int(o + a + h)



def find_tris_for_perimiter(p):
    tris = []
    for x in xrange(1,p):
        for y in range(x,p) :
            if check_integer_tri(p, x, y):
                tris.append((x,y))
    return tris

def count_tris_for_perimiter(p):
    return len(find_tris_for_perimiter(p))


def interger_sides_for_p(limit=1001):
    return list(reversed(sorted([(count_tris_for_perimiter(p),p) for p in xrange(limit)])))

#print check_integer_tri(12,3,4)

# print count_tris_for_perimiter(120)
print interger_sides_for_p()