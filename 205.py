from collections import Counter


def roll_dice(faces,iterations):
	if iterations == 1:
		return range(1, faces+1)
	rolls = roll_dice(faces, iterations-1)
	return [x + y for x in rolls for y in range(1, faces+1)]



# def counter_to_

print 6 ** 6
print 4 ** 9

print roll_dice(6,2)

cube_rolls = roll_dice(6,6)
pyramid_rolls = roll_dice(4,9)
cube_counter = Counter(cube_rolls)
pyramid_counter = Counter(pyramid_rolls)


pyramid_rolls_that_win = 0
pyramid_rolls_that_lose = 0
total_count = 0

for cube_item, cube_count in cube_counter.items():



	for pyramid_item, pyramid_count in pyramid_counter.items():
		total_count += pyramid_count * cube_count
		if pyramid_item > cube_item:
			pyramid_rolls_that_win += pyramid_count * cube_count

print float(pyramid_rolls_that_win) / total_count

