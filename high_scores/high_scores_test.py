import unittest

from high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    # Tests
    def setUp(self):
        self.score_1 = [6, 8, 3, 1, 9, 4]
        self.score_2 = [8, 7, 4, 9, 3, 8]
        self.score_3 = [8, 4]
        self.score_4 = [7]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(4, latest(self.score_1))

    # Test personal best (the highest score in the list)

    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    

if __name__ == "__main__":
    unittest.main()
