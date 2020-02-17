#!/usr/bin/env python3

from mastermind.board import Board
from mastermind.player import Player
from mastermind.score import Score
import unittest


class Score_Test(unittest.TestCase):
    """
    Tests for the Score class.
    """

    def test_apply_victory_bonus(self):
        """
        Test apply_victory_bonus() for correct return values.
        """
        board = Board(4, True)
        player = Player("Tu", "1")
        score = Score(board, player, False, 0)
        self.assertTrue(score.apply_victory_bonus(), 100000)
        player = Player("Tu", "1")
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_victory_bonus(), 200000)
        player = Player("Tu", "2")
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_victory_bonus(), 400000)
        player = Player("Tu", "3")
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_victory_bonus(), 800000)
        player = Player("Tu", "4")
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_victory_bonus(), 1600000)

    def test_apply_time_penalty(self):
        """
        Test apply_time_penalty() for correct return values.
        """
        board = Board(4, True)
        player = Player("Tu", "1")
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_time_penalty(), 100000)
        score = Score(board, player, True, 50)
        self.assertTrue(score.apply_time_penalty(), 75000)
        score = Score(board, player, True, 100)
        self.assertTrue(score.apply_time_penalty(), 50000)
        score = Score(board, player, True, 200)
        self.assertIs(int(score.apply_time_penalty()), 0)
        score = Score(board, player, True, 250)
        self.assertIs(int(score.apply_time_penalty()), 0)

    def test_apply_turn_bonus(self):
        """
        Test apply_turn_bonus() for correct return values.
        """
        board = Board(4, True)
        player = Player("Tu", "1")
        player.turns = 12
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_turn_bonus(), 200000)
        player.turns = 6
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_turn_bonus(), 150000)
        player.turns = 0
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_turn_bonus(), 100000)
        player = Player("Tu", "4")
        player.turns = 6
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_turn_bonus(), 200000)
        player.turns = 3
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_turn_bonus(), 150000)
        player.turns = 0
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_turn_bonus(), 100000)

    def test_apply_hint_penalty(self):
        """
        Test apply_hint_penalty() for correct return values.
        """
        board = Board(4, True)
        board.hints_remaining = [0, 1, 2, 3]
        player = Player("Tu", "1")
        score = Score(board, player, True, 0)
        self.assertTrue(score.apply_hint_penalty(), 100000)
        board.hints_remaining = [0, 1, 2]
        self.assertTrue(score.apply_hint_penalty(), 750000)
        board.hints_remaining = [0, 1]
        self.assertTrue(score.apply_hint_penalty(), 50000)
        board.hints_remaining = [0]
        self.assertTrue(score.apply_hint_penalty(), 25000)


if __name__ == '__main__':
    unittest.main()
