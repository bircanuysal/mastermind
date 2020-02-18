#!/usr/bin/env python3

from mastermind.history import History
import unittest


class History_Test(unittest.TestCase):
    """
    Tests for the History class.
    """

    def test_generate_history(self):
        """
        Test test_generate_history() for correct return values.
        """
        sb = History()
        sb.player_guesses.append([1, 2, 3, 4])
        sb.player_scores.append({"correct_colors": 1,
                                 "correct_positions": 3})
        res = sb.generate_history()
        self.assertTrue(len(res), 1)
        sb.player_guesses.append([5, 6, 7, 0])
        sb.player_scores.append({"correct_colors": 2,
                                 "correct_positions": 2})
        res = sb.generate_history()
        self.assertTrue(len(res), 2)


if __name__ == '__main__':
    unittest.main()
