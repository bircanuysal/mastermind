#!/usr/bin/env python3

from mastermind.board import Board
from mastermind.player import Player


class Score:
    """
    Score class.
    """

    def __init__(self, board: Board, player: Player, victory: bool, time: int):
        """
        Score constructor.
        """
        self.base_score = 100000
        self.board = board
        self.player = player
        self.victory = victory
        self.time = time

    def final_score(self):
        """
        Calculates final score after applying all multipliers.
        """
        self.apply_victory_bonus()
        self.apply_time_penalty()
        self.apply_turn_bonus()
        self.apply_hint_penalty()
        return round(self.base_score)

    def apply_victory_bonus(self) -> int:
        """
        Applies bonus based on if the player has won or not.
        Lose              = No bonus
        Win on Easy       = +200% bonus
        Win on Medium     = +400% bonus
        Win on Hard       = +800% bonus
        Win on Dark Souls = +1600% bonus
        """
        if self.victory:
            self.base_score <<= int(self.player.difficulty)
        return self.base_score

    def apply_time_penalty(self) -> int:
        """
        Applies penalty based on the duration of the game.
        10 seconds   = -5% reduction
        25 seconds   = -12% reduction
        50 seconds   = -25% reduction
        100 seconds  = -50% reduction
        200+ seconds = -100% reduction
        """
        time_penalty = (self.time / 100)
        time_penalty = time_penalty if time_penalty <= 2 else 2
        self.base_score *= 1 - (time_penalty / 2)
        return self.base_score

    def apply_turn_bonus(self):
        """
        Applies a bonus based on the percentage of turns left.
        0/10 turns left = No bonus
        5/10 turns left = +50% bonus
        9/10 turns left = +90% bonus
        """
        turn_map = {"1": 12, "2": 10, "3": 8, "4": 6}
        total_turns = turn_map.get(self.player.difficulty)
        turns_remaining = self.player.turns
        self.base_score *= 1 + (turns_remaining / total_turns)
        return self.base_score

    def apply_hint_penalty(self):
        """
        Applies hint penalty for every hint used.
        1 hint used  = -25% reduction
        2 hints used = -50% reduction
        3 hints used = -75% reduction
        4 hints used = -100% reduction
        """
        hints_used = self.board.num_count - len(self.board.hints_remaining)
        print(f"Hints used: {hints_used}.")
        hint_penalty = hints_used / self.board.num_count
        self.base_score -= hint_penalty * self.base_score
        return self.base_score
