"""
An implementation of instant runoff voting with arbitrary tie breaking.
"""

from collections import Counter
import unittest
import logging

class Vote:
    """Holds a ranked list of preferences"""

    def __init__(self, *preferences):
        self.preferences = preferences

    def get_preference(self, elminated = ()):
        """Retrieves the top preference (or None), subject to any eliminated candidates"""
        cleaned_preferences = filter(lambda x: x not in elminated, self.preferences)
        if cleaned_preferences:
            return cleaned_preferences[0]


class TestVote(unittest.TestCase):

    def test_single_preference(self):
        prefernce = "Alice"
        vote = Vote(prefernce)
        self.assertEqual(prefernce, vote.get_preference())

    def test_multiple_preferences(self):
        prefernce1, prefernce2 = "Bob", "Alice"
        vote = Vote(prefernce1, prefernce2)
        self.assertEqual(prefernce1, vote.get_preference())

    def test_blank_preferences(self):
        vote = Vote()
        self.assertIsNone(vote.get_preference())

    def test_elimated_first_preference(self):
        prefernce1, prefernce2 = "Bob", "Alice"
        vote = Vote(prefernce1, prefernce2)
        self.assertEqual(prefernce2, vote.get_preference([prefernce1]))

    def test_elimated_second_preference(self):
        prefernce1, prefernce2 = "Bob", "Alice"
        vote = Vote(prefernce1, prefernce2)
        self.assertEqual(prefernce1, vote.get_preference([prefernce2]))

    def test_completely_elmininated_preferences(self):
        prefernce1, prefernce2 = "Bob", "Alice"
        vote = Vote(prefernce1, prefernce2)
        self.assertIsNone(vote.get_preference([prefernce1, prefernce2]))



class Election:

    def __init__(self, votes):
        self.votes = votes

    def get_winner(self, elminated = None):
        if len(self.votes) == 0:
            logging.warning("\tParticipate in the democratic process!")
            return None
        if elminated is None:
            elminated = []
        tally = self.tally_votes(elminated)
        if self.candidate_has_majority(tally):
            winner = tally.most_common(1)[0][0]
            logging.info("\tWinner: {}".format(winner))
            return tally.most_common(1)[0][0]
        else:
            if self.tie(tally):
                logging.warning("\tCrap, there's a tie. Resolving arbitrarily.")
            last_place = tally.most_common()[-1][0]
            logging.info("\t{} eliminated.".format(last_place))
            return self.get_winner(elminated + [last_place])

    def tally_votes(self, elminated):
        ranked = Counter([vote.get_preference(elminated) for vote in self.votes if vote.get_preference(elminated)])

        logging.info("\tStandings with {} eliminated:".format(elminated))
        logging.info("\t\t{}".format(ranked))
        return ranked

    def candidate_has_majority(self, tally):
        total = sum([tally[key] for key in tally])
        return tally.most_common(1)[0][1] > total / 2

    def tie(self, tally):
        return len(tally) > 1 and tally.most_common()[-1][1] == tally.most_common()[-2][1]

class TestElection(unittest.TestCase):

    def test_no_votes(self):
        votes = []
        election = Election(votes)
        self.assertIsNone(election.get_winner())

    def test_single_vote(self):
        prefernce1, prefernce2 = "Bob", "Alice"
        votes = [
            Vote(prefernce1, prefernce2)
        ]
        election = Election(votes)
        self.assertEqual(prefernce1, election.get_winner())

    def test_simple_election(self):
        candidate1, candidate2, candidate3 = "Alice", "Bob", "Charlie"
        votes = [
            Vote(candidate1),
            Vote(candidate1),
            Vote(candidate2),
            Vote(candidate2),
            Vote(candidate3, candidate1)
        ]
        election = Election(votes)
        self.assertEqual(candidate1, election.get_winner())

    def test_renegade_voter(self):
        """ Encountered a bug when all a voter's preferences were eliminated"""
        candidate1, candidate2, candidate3 = "Alice", "Bob", "Charlie"
        candidate4, candidate5 = "Edward", "Fox"
        votes = [
            Vote(candidate1),
            Vote(candidate1),
            Vote(candidate2),
            Vote(candidate2),
            Vote(candidate3, candidate1),
            Vote(candidate4, candidate5)
        ]
        election = Election(votes)
        self.assertEqual(candidate1, election.get_winner())

def run_election():
    test_votes = [
        Vote("Alice" ,"Bob", "Charlie"),
        Vote("Alice" ,"Bob", "Charlie"),
        Vote("Bob", "Charlie", "Alice"),
        Vote("Charlie", "Alice" ,"Bob"),
        Vote("Bob" ,"Bob", "Charlie"),
        Vote("Dave" ,"Edward", "Kasper"),
        Vote("Dave" ,"Bob", "Charlie"),
    ]

    election = Election(test_votes)
    election.get_winner()

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run_election()
    logging.getLogger().setLevel(logging.ERROR)
    unittest.main()
