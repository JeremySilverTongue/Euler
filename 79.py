

with open("p079_keylog.txt") as keys:
	data = [line.strip() for line in keys]



# def add_key(passcode, key):
# 	last_char_position = -1
# 	last_char = ""
# 	for char in key:
# 		x = len(passcode) - 1
# 		found = False
# 		while x > last_char_position:
# 			if passcode[x] == char:
# 				found = True
# 				break
# 			if passcode[x-1] == last_char:
# 				break
# 			x -= 1
# 		if not found:
# 			passcode.insert(last_char_position+1,char)
# 	return passcode


def check_key(passcode, keys):

	for key in keys:
		passcode_index = 0
		for char in key:
			found = False
			while passcode_index < len(passcode):
				if passcode[passcode_index] == char:
					found = True
					break
				passcode_index += 1
			if not found:
				return False
	return True
	



# print add_key([],"123")

# print "12344".find("4")

# print check_key("123456",data)

print data
for x in xrange(1000000000):
	if check_key(str(x), data):
		print x
		break







