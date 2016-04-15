def generate_triangular_numbers(terms):
    return [n * (n + 1) / 2 for n in range(terms)]


FILE_NAME = "p042_words.txt"


def parse_words(file_name=FILE_NAME):
    with open(file_name) as words:
        return words.read().strip('"').split('","')


values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}


def alphabetical_value(input):
    value = 0
    for letter in input:
        value += values[letter]
    return value


def find_triangular_words(words, triangular_numbers):
    count = 0
    for word in words:
        if alphabetical_value(word) in triangular_numbers:
            count += 1
    return count


print generate_triangular_numbers(100)
words = parse_words()
triangular_numbers = generate_triangular_numbers(100)
print find_triangular_words(words, triangular_numbers)
