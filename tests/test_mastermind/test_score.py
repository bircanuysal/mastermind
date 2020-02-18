#!/usr/bin/env python3

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
        player = Player("Tu", "1")
        score = Score(player, False, 0, 4, 4)
        self.assertEquals(score.apply_victory_bonus(), 100000)
        player = Player("Tu", "1")
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_victory_bonus(), 200000)
        player = Player("Tu", "2")
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_victory_bonus(), 400000)
        player = Player("Tu", "3")
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_victory_bonus(), 800000)
        player = Player("Tu", "4")
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_victory_bonus(), 1600000)

    def test_apply_time_penalty(self):
        """
        Test apply_time_penalty() for correct return values.
        """
        player = Player("Tu", "1")
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_time_penalty(), 100000)
        score = Score(player, True, 50, 4, 4)
        self.assertEquals(score.apply_time_penalty(), 75000)
        score = Score(player, True, 100, 4, 4)
        self.assertEquals(score.apply_time_penalty(), 50000)
        score = Score(player, True, 200, 4, 4)
        self.assertEquals(int(score.apply_time_penalty()), 0)
        score = Score(player, True, 250, 4, 4)
        self.assertEquals(int(score.apply_time_penalty()), 0)

    def test_apply_turn_bonus(self):
        """
        Test apply_turn_bonus() for correct return values.
        """
        player = Player("Tu", "1")
        player.turns = 12
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_turn_bonus(), 200000)
        player.turns = 6
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_turn_bonus(), 150000)
        player.turns = 0
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_turn_bonus(), 100000)
        player = Player("Tu", "4")
        player.turns = 6
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_turn_bonus(), 200000)
        player.turns = 3
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_turn_bonus(), 150000)
        player.turns = 0
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_turn_bonus(), 100000)

    def test_apply_hint_penalty(self):
        """
        Test apply_hint_penalty() for correct return values.
        """
        player = Player("Tu", "1")
        score = Score(player, True, 0, 4, 4)
        self.assertEquals(score.apply_hint_penalty(), 100000)
        score = Score(player, True, 0, 4, 3)
        self.assertEquals(score.apply_hint_penalty(), 75000)
        score = Score(player, True, 0, 4, 2)
        self.assertEquals(score.apply_hint_penalty(), 50000)
        score = Score(player, True, 0, 4, 1)
        self.assertEquals(score.apply_hint_penalty(), 25000)
        score = Score(player, True, 0, 4, 0)
        self.assertEquals(int(score.apply_hint_penalty()), 0)


if __name__ == '__main__':
    unittest.main()
