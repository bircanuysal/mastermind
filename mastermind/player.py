#!/usr/bin/env python3

from mastermind.scoreboard import Scoreboard


class Player:
    """
    Player class.
    """

    def __init__(self, name: str, difficulty: str):
        """
        Player constructor.
        """
        turn_map = {"1": 12, "2": 10, "3": 8, "4": 6}
        self.name = name
        self.difficulty = difficulty
        self.turns = turn_map.get(self.difficulty)

    def check_victory(self, num_count: int, scoreboard: Scoreboard) -> bool:
        """
        Checks if the current player has won the game.
        """
        last_score = scoreboard.player_scores[-1]
        return last_score.get("correct_positions") == num_count

    def check_defeat(self) -> bool:
        """
        Checks if the current player has lost the game.
        """
        return self.turns == 0
