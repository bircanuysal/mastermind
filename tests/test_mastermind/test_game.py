#!/usr/bin/env python3

from mastermind.board import Board
from mastermind.game import Game
from mastermind.player import Player
from mastermind.scoreboard import Scoreboard
import unittest


class Game_Test(unittest.TestCase):
    """
    Tests for the Game class.
    """

    def test_check_victory_truthy(self):
        """
        Test check_victory() for truthy returns.
        """
        game = Game()
        board = Board(7, True)
        scoreboard = Scoreboard()
        board.scoreboard = scoreboard
        scoreboard.player_scores = [
            {"correct_colors": 0, "correct_positions": 4}]
        self.assertTrue(game.check_victory(board))

    def test_check_victory_falsy(self):
        """
        Test check_victory() for falsy returns.
        """
        game = Game()
        board = Board(7, True)
        scoreboard = Scoreboard()
        board.scoreboard = scoreboard
        scoreboard.player_scores = [
            {"correct_colors": 1, "correct_positions": 3}]
        self.assertFalse(game.check_victory(board))
        scoreboard.player_scores = [
            {"correct_colors": 2, "correct_positions": 2}]
        self.assertFalse(game.check_victory(board))
        scoreboard.player_scores = [
            {"correct_colors": 3, "correct_positions": 1}]
        self.assertFalse(game.check_victory(board))
        scoreboard.player_scores = [
            {"correct_colors": 4, "correct_positions": 0}]
        self.assertFalse(game.check_victory(board))

    def test_check_defeat_truthy(self):
        """
        Test check_defeat() for truthy returns.
        """
        game = Game()
        player = Player("Tu", "2")
        player.turns = 0
        self.assertTrue(game.check_defeat(player))

    def test_check_defeat_falsy(self):
        """
        Test check_defeat() for falsy returns.
        """
        game = Game()
        player = Player("Tu", "2")
        self.assertFalse(game.check_defeat(player))
        player.turns = 2
        self.assertFalse(game.check_defeat(player))
        player.turns = 1
        self.assertFalse(game.check_defeat(player))


if __name__ == '__main__':
    unittest.main()
