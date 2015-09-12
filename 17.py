

small = {
	0 : "",
	1 : "one",
	2 : "two",	
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",							
	11 : "eleven",
	12 : "twelve",
	13 : "thirteen",
	14 : "fourteen",
	15 : "fifteen",
	16 : "sixteen",
	17 : "seventeen",
	18 : "eighteen",
	19 : "nineteen",
	20 : "twenty",
	30 : "thirty",	
	40 : "forty",
	50 : "fifty",
	60 : "sixty",
	70 : "seventy",
	80 : "eighty",
	90 : "ninety",
	1000 : "one thousand"				
}

HUNDRED_STRING = " hundred "
AND_STRING = "and "


def pretty_number(n):
	if n == 0:
		return ""
	if n in small:
		return small[n]

	working_number = n


	hundreds, working_number = divmod(working_number,100)
	if hundreds > 0:
		remaining_rep = pretty_number(working_number) 
		rep = pretty_number(hundreds) + HUNDRED_STRING
		if remaining_rep:
			rep += AND_STRING + remaining_rep 
		return rep
	tens, working_number = divmod(working_number,10)
	if tens > 0:
		return pretty_number(tens * 10) + " " + pretty_number(working_number)

def total_letters(lower, upper):
	total = 0
	for x in range(lower, upper+1):
		total += len( pretty_number(x).replace(" ", ""))
	return total

#for x in range(1001):
#	print pretty_number(x)


print total_letters(1,1000)
