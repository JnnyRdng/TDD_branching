import unittest

from high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    # Tests
    def setUp(self):
        self.scores_1 = [6, 8, 3, 1, 9, 4]
        self.scores_2 = [8, 7, 4, 9, 3, 8]
        self.scores_3 = [8, 4]
        self.scores_4 = [7]

    # Test latest score (the last thing in the list)
    def test_latest_scores(self):
        self.assertEqual(4, latest(self.scores_1))

    # Test personal best (the highest scoresin the list)
    def test_highest_scores(self):
        self.assertEqual(9, personal_best(self.scores_1))

    # Test top three from list of scores
    def test_return_3_from_list(self):
        self.assertEqual(3, len(personal_top_three(self.scores_1)))

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    

if __name__ == "__main__":
    unittest.main()
