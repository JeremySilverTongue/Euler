def isLeapYear(year):
    if not year % 4 == 0:
        return False
    elif not year % 100 == 0:
        return True
    elif year % 400 == 0:
        return True
    return False

def monthLength(year, month):
    if isLeapYear(year) and month == 2:
        return 29
    return [31,28,31,30,31,30,31,31,30,31,30,31][month-1]

def nextDay(year, month, day):
	# year, month, day = date
    currentMonthLength = monthLength(year, month)
    if month > 12 or day > currentMonthLength:
        print "Not a valid date, bro."
        return year, month, day
    
    newDay = day + 1
    newMonth = month
    newYear = year
    
    if newDay > currentMonthLength:
        newDay -= currentMonthLength
        newMonth +=1
    if newMonth > 12:
        newMonth -= 12
        newYear += 1
    return newYear, newMonth, newDay

def datesEqual(year1, month1, day1, year2, month2, day2):
    return year1 == year2 and month1 == month2 and day1 == day2

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while (not datesEqual(year1, month1, day1, year2, month2, day2)):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
        
def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert(dateIsAfter(year2, month2, day2, year1, month1, day1))
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days

def days_since_1900_to_day_of_week(n):
	return translation[n % 7]

translation = {
	0 : "Monday",
	1 : "Tuesday",
	2 : "Wednesday",	
	3 : "Thursday",
	4 : "Friday",
	5 : "Saturday",
	6 : "Sunday"
}

days_since_1900 = {
	# (1900, 1, 1) : (0, 0)
}            

def fill_days_since_1900():
	start = (1900, 1, 1)
	days_since = 0
	end = (2000, 12, 31)
	current = start
	while dateIsAfter( end[0], end[1], end[2], current[0], current[1], current[2]):
		days_since_1900[current] = days_since, days_since % 7
		days_since += 1
		current = nextDay(current[0], current[1], current[2])

def find_sundays_on_the_first():
	return [(key, value) for key, value in days_since_1900.iteritems() if key[2] == 1 and value[1]==6 and dateIsAfter(key[0], key[1], key[2], 1901, 1,1)]

fill_days_since_1900()
# print days_since_1900
sundays = find_sundays_on_the_first()
print sundays
print len(sundays)






# print days_since_1900