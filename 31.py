from collections import Counter


coins = [200, 100, 50, 20, 10, 5, 2, 1]
# coins = [2, 1]

# coins = [1,2,5,10,20,50,100,200]

# def counter_

def make_change(value, coins_to_use = coins):
	# print "Making change for", value, "using", coins_to_use
	if value == 0:
		return 1
	total = 0
	for x in range(len(coins_to_use)):
		coin = coins_to_use[x]
		remaining_coins = coins_to_use[x:]
		if coin <= value:
			total += make_change(value - coin, remaining_coins)
	# print "found", total, "ways to make change for", value,"using", coins_to_use
	return total


# count = Counter([1])
# count.update([1])
# print count

# print make_change(1)
print make_change(200,coins)

# print make_change(1, Counter({1: 1}), [Counter({2: 1}), Counter({1: 1})])




# print tuple(Counter([1,2,3,4,4]).items())