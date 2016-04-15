CONVERSION = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_geq(num1, num2):
    numeral_order = "IVXLCDM"
    return numeral_order.find(num1) >= numeral_order.find(num2)


def roman_to_integer(numeral):
    if len(numeral) == 1:
        return CONVERSION[numeral]
    elif len(numeral) == 2:
        return CONVERSION[numeral[1]] - CONVERSION[numeral[0]]
    else:
        print "Borked numeral", numeral
        return -1


def parse_roman_numeral(numeral):
    total = 0
    m_numeral = numeral[:].strip()
    while m_numeral:
        if len(m_numeral) == 1:
            total += roman_to_integer(m_numeral)
            return total
        if not roman_geq(m_numeral[0], m_numeral[1]):
            total += roman_to_integer(m_numeral[:2])
            m_numeral = m_numeral[2:]
        else:
            total += roman_to_integer(m_numeral[0])
            m_numeral = m_numeral[1:]
    return total


def int_to_roman_numeral(integer):
    if integer == 0:
        return ""
    if integer >= 1000:
        return "M" + int_to_roman_numeral(integer - 1000)
    if integer >= 900:
        return "CM" + int_to_roman_numeral(integer - 900)
    if integer >= 500:
        return "D" + int_to_roman_numeral(integer - 500)
    if integer >= 400:
        return "CD" + int_to_roman_numeral(integer - 400)
    if integer >= 100:
        return "C" + int_to_roman_numeral(integer - 100)
    if integer >= 90:
        return "XC" + int_to_roman_numeral(integer - 90)
    if integer >= 50:
        return "L" + int_to_roman_numeral(integer - 50)
    if integer >= 40:
        return "XL" + int_to_roman_numeral(integer - 40)
    if integer >= 10:
        return "X" + int_to_roman_numeral(integer - 10)
    if integer >= 9:
        return "IX" + int_to_roman_numeral(integer - 9)
    if integer >= 5:
        return "V" + int_to_roman_numeral(integer - 5)
    if integer >= 4:
        return "IV" + int_to_roman_numeral(integer - 4)
    if integer >= 1:
        return "I" + int_to_roman_numeral(integer - 1)

for x in range(100):
    print x, int_to_roman_numeral(x)


def minimize_numeral(num):
    return int_to_roman_numeral(parse_roman_numeral(num))
# print roman_geq("I", "X")
# print parse_roman_numeral("IX")


savings = 0
with open("p089_roman.txt") as numerals:
    for line in numerals:
        stripped = line.strip()
        print stripped, minimize_numeral(stripped)
        savings += len(stripped) - len(minimize_numeral(stripped))

print savings
