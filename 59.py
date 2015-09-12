from nltk.corpus import wordnet



with open("p059_cipher.txt") as cipher:
	data = map(int,cipher.read().split(","))

# print data

def check_contains_english_word(string):
	words = string.split()
	for word in words:
		if wordnet.synsets(word):
			return True
	return False


# # def partition(list, size):

def ints_to_string(ints):
	return "".join(map(chr, ints))

def decode(message, key):

	decoded = []
	for x in range(len(message)):
		decoded.append(message[x] ^ ord(key[x % len(key)]))
	return decoded

def check_key(message, key):
	decoded_ints = decode(message, key)
	decoded_string = ints_to_string(decoded_ints)

	if check_contains_english_word(decoded_string):
		print key, sum(decoded_ints), decoded_string, "\n"

candidate_range = range(ord('a'), ord('z')+1)

# # for key_letter_1 in candidate_range:
# 	for key_letter_2 in candidate_range:
# 		# for key_letter_3 in candidate_range:
# 			# key = chr(key_letter_1) + chr(key_letter_2) + chr(key_letter_3)
# 			key = "g" + chr(key_letter_2) + "x"
# 			check_key(data, key)

for key_letter_2 in candidate_range:
			# key = chr(key_letter_1) + chr(key_letter_2) + chr(key_letter_3)
			key = "g" + "o" + chr(key_letter_2)
			check_key(data, key)



# print check_key(data, "abc")
# # print check_contains_english_word("asdfasdfasdfasdf")
# # print check_contains_english_word("asdfasdf butt  hello asdfasdf")


# print zip("123456789","123")