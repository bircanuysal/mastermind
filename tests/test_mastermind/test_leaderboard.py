#!/usr/bin/env python3

from mastermind.leaderboard import Leaderboard
import unittest


class Leaderboard_Test(unittest.TestCase):
    """
    Tests for the Leaderboard class.
    """

    def test_open_leaderboard_truthy(self):
        """
        Test open_leaderboard() for truthy returns.
        """
        Leaderboard.file_path = "data/leaderboard.json"
        res = Leaderboard.open_leaderboard()
        self.assertTrue(res)

    def test_open_leaderboard_falsy(self):
        """
        Test open_leaderboard() for falsy returns.
        """
        Leaderboard.file_path = "test.json"
        res = Leaderboard.open_leaderboard()
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
