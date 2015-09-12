import unittest
from collections import Counter



class PlayingCard:

	def rank_to_int(self, rank):
		if rank == "J":
			return 11
		elif rank == "Q":
			return 12
		elif rank == "K":
			return 13
		elif rank == "A":
			return 14
		else:
			return int(rank)

	def printable_rank(self):
		if self.rank == 11:
			return "Jack"
		elif self.rank == 12:
			return "Queen"
		elif self.rank == 13:
			return "King"
		elif self.rank == 14:
			return "Ace"
		else:
			return str(self.rank)

	def printable_suit(self):
		if self.suit == "H":
			return "Hearts"
		elif self.suit == "C":
			return "Clubs"
		elif self.suit == "S":
			return "Spades"
		else:
			return "Dimonds"

	def __init__(self, string):
		self.rank = self.rank_to_int(string[0])
		self.suit = string[1]

	def __repr__(self):
		return "The {} of {}".format(self.printable_rank(), self.printable_suit())

class PokerHandScore:

	ROYAL_FLUSH = 9
	STRAIGHT_FLUSH = 8
	FOUR_OF_A_KIND = 7
	FULL_HOUSE = 6
	FLUSH = 5
	STRAIGHT = 4
	THREE_OF_A_KIND = 3
	TWO_PAIRS = 2
	ONE_PAIR = 1
	HIGH_CARD = 0

	def __init__(self, score):
		self.score = score

	def __repr__(self):
		if self.score[0] == self.ROYAL_FLUSH:
			return "Royal"

class PokerHand:

	def __init__(self, string):
		self.cards = []
		for card_string in string.split():
			self.cards.append(PlayingCard(card_string))

	def __repr__(self):
		return "A poker hand containing: {}".format(self.cards)


	def score_hand(self):
		if self.has_straight_flush():
			return self.score_stright_flush()
		elif self.has_four_of_a_kind():
			return self.score_one_pair()
		elif self.has_full_house():
			return self.score_full_house()			
		elif self.has_flush():
			return self.score_flush()
		elif self.has_straight():
			return self.score_straight()
		elif self.has_three_of_a_kind():
			return self.score_three_of_a_kind()
		elif self.has_two_pairs():
			return self.score_two_pairs()
		elif self.has_one_pair():
			return self.score_one_pair()
		else:
			return self.score_high_card()
															
	def has_flush(self):
		return all(map(lambda card: self.cards[0].suit == card.suit, self.cards))

	def score_flush(self):
		return (0,0,0,0,0)

	def has_straight(self):
		return False

	def score_straight(self):
		return (0,0,0,0,0)		

	def has_straight_flush(self):
		return self.has_flush() and self.has_straight()

	def score_straight_flush(self):
		return (0,0,0,0,0)			

	def has_four_of_a_kind(self):
		return False

	def score_four_of_a_kind(self):
		return (0,0,0,0,0)			

	def has_full_house(self):
		return False

	def score_full_house(self):
		return (0,0,0,0,0)			

	def has_three_of_a_kind(self):
		return False

	def score_three_of_a_kind(self):
		return (0,0,0,0,0)			

	def has_two_pairs(self):
		ranks = [card.rank for card in self.cards]
		ranks_counter = Counter(ranks)
		most_common = ranks_counter.most_common(2)
		return 2 == most_common[0][1] == most_common[0][1]

	def score_two_pairs(self):
		return (0,0,0,0,0)			

	def has_one_pair(self):
		ranks = [card.rank for card in self.cards]
		return 2 == Counter(ranks).most_common(1)[0][1]

	def score_one_pair(self):
		ranks = [card.rank for card in self.cards]
		pair_rank = Counter(ranks).most_common(1)[0][0]
		tie_breakers = tuple(reversed(sorted([rank for rank in ranks if rank != pair_rank])))
		return (PokerHandScore.ONE_PAIR,pair_rank) + tie_breakers

	def score_high_card(self):
		return (PokerHandScore.HIGH_CARD,) +tuple(reversed(sorted([card.rank for card in self.cards])))

	


# card = PlayingCard("5H")
# flush_hand = PokerHand("5H 5C 6S 7S KD")
# print flush_hand.has_one_pair()
# print flush_hand.score_one_pair()
# print hand 
# print hand.has_flush()


print sorted([ (2,4),(2,5),(1,5),(1,)])

class TestPokerHands(unittest.TestCase):

	def test_two_pair(self):
		not_flush_hand = PokerHand("5H 5H 6H 7H KC")
		self.assertFalse(not_flush_hand.has_flush())


	def test_flush(self):
		flush_hand = PokerHand("5H 5H 6H 7H KH")
		self.assertTrue(flush_hand.has_flush())

	def test_not_flush(self):
		not_flush_hand = PokerHand("5H 5H 6H 7H KC")
		self.assertFalse(not_flush_hand.has_flush())



	def test_high_card_score(self):
		high_card_hand = PokerHand("5H 5H 6H 7H KC")
		self.assertEqual(high_card_hand.score_high_card(), (0,13, 7, 6, 5, 5))



if __name__ == '__main__':
	unittest.main()


