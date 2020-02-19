#!/usr/bin/env python3

from mastermind.board import Board
from mastermind.history import History
import unittest


class Board_Test(unittest.TestCase):
    """
    Tests for the Board class.
    """

    def test_generate_numbers_locally(self):
        """
        Test generate_numbers_locally() for correct return type and values.
        """
        board = Board(1, None, True)
        res = board.generate_numbers_locally()
        self.assertTrue(type(res) == list)
        self.assertTrue(len(res) == 4)
        self.assertTrue(all([type(i) == int for i in res]))
        self.assertTrue(all([7 >= int(i) >= 0 for i in res]))

        board = Board(4, None, True)
        res = board.generate_numbers_locally()
        self.assertTrue(type(res) == list)
        self.assertTrue(len(res) == 4)
        self.assertTrue(all([type(i) == int for i in res]))
        self.assertTrue(all([9 >= int(i) >= 0 for i in res]))

    @unittest.skip("To reduce the chance of going over rate limits.")
    def test_generate_numbers_with_API(self):
        """
        Test generate_numbers_with_API() for correct return type and values.
        """
        board = Board(1, None, True)
        res = board.generate_numbers_with_API()
        self.assertTrue(type(res) == list)
        self.assertTrue(len(res) == 4)
        self.assertTrue(all([type(i) == int for i in res]))
        self.assertTrue(all([7 >= int(i) >= 0 for i in res]))

    def test_check_board_00(self):
        """
        Test check_board() for correct return type and values.
        """
        board = Board(1, [1, 2, 3, 4], False)
        history = History()
        board.history = history
        history.player_guesses = [[1, 2, 3, 4]]
        self.assertDictEqual(board.check_board(),
                             {"correct_colors": 0,
                              "correct_positions": 4})

    def test_check_board_01(self):
        """
        Test check_board() for correct return type and values.
        """
        board = Board(1, [1, 2, 3, 4], False)
        history = History()
        board.history = history
        history.player_guesses = [[5, 6, 7, 0]]
        self.assertDictEqual(board.check_board(),
                             {"correct_colors": 0,
                              "correct_positions": 0})

    def test_check_board_02(self):
        """
        Test check_board() for correct return type and values.
        """
        board = Board(1, [1, 2, 3, 4], False)
        history = History()
        board.history = history
        history.player_guesses = [[1, 1, 1, 1]]
        self.assertDictEqual(board.check_board(),
                             {"correct_colors": 0,
                              "correct_positions": 1})

    def test_check_board_03(self):
        """
        Test check_board() for correct return type and values.
        """
        board = Board(1, [1, 2, 3, 4], False)
        history = History()
        board.history = history
        history.player_guesses = [[1, 4, 2, 3]]
        self.assertDictEqual(board.check_board(),
                             {"correct_colors": 3,
                              "correct_positions": 1})

    def test_check_board_04(self):
        """
        Test check_board() for correct return type and values.
        """
        board = Board(1, [2, 2, 5, 5], False)
        history = History()
        board.history = history
        history.player_guesses = [[2, 2, 2, 2]]
        self.assertDictEqual(board.check_board(),
                             {"correct_colors": 0,
                              "correct_positions": 2})

    def test_generate_hint_truthy(self):
        """
        Test generate_hint() for truthy returns.
        """
        board = Board(1, None, True)
        self.assertTrue(board.generate_hint())

    def test_generate_hint_falsy(self):
        """
        Test generate_hint() for falsy returns.
        """
        board = Board(1, None, True)
        for _ in range(4):
            board.generate_hint()
        self.assertFalse(board.generate_hint())


if __name__ == '__main__':
    unittest.main()
