#!/usr/bin/env python3

from mastermind.history import History
from mastermind.leaderboard import Leaderboard
from mastermind.score import Score
from typing import List, Dict


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

    def check_victory(self, num_count: int,
                      player_scores: List[Dict[str, str]]) -> bool:
        """
        Checks if the current player has won the game.
        """
        last_score = player_scores[-1]
        return last_score.get("correct_positions") == num_count

    def check_defeat(self) -> bool:
        """
        Checks if the current player has lost the game.
        """
        return self.turns == 0

    def calculate_score(self, victory: bool, time: int,
                        num_count: int, hints_remaining: int):
        """
        Calculates player score based on victory status, time, difficulty and
        turns remaining.
        """
        s = Score(self, victory, time, num_count, hints_remaining)
        score = s.final_score()
        print(f"Your score was {score}.")
        Leaderboard.write_score(self.name, score)
