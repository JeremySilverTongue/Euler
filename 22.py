

FILE_NAME = "p022_names.txt"

def load_and_sort_names(file_name = FILE_NAME):
	with open(file_name) as names_file:
		return sorted(names_file.read().strip('"').split('","'))


values = {
	'A' : 1,
	'B' : 2,	
	'C' : 3,
	'D' : 4,
	'E' : 5,
	'F' : 6,	
	'G' : 7,
	'H' : 8,
	'I' : 9,
	'J' : 10,	
	'K' : 11,
	'L' : 12,
	'M' : 13,
	'N' : 14,	
	'O' : 15,
	'P' : 16,
	'Q' : 17,
	'R' : 18,	
	'S' : 19,
	'T' : 20,
	'U' : 21,
	'V' : 22,	
	'W' : 23,
	'X' : 24,
	'Y' : 25,
	'Z' : 26
}
		
def alphabetical_value(input):
	value = 0
	for letter in input:
		value += values[letter]
	return value


def total_score(names):
	score = 0
	for x in range(len(names)):
		score += (x+1) * alphabetical_value(names[x])
	return score


names = load_and_sort_names()

print total_score(names)




