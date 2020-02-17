#!/usr/bin/env python3


class Player:
    """
    Player class.
    """

    def __init__(self, name: str, difficulty: int):
        """
        Player constructor.
        """
        turn_map = {"1": 12, "2": 10, "3": 8, "4": 6}
        self.name = name
        self.difficulty = difficulty
        self.turns = turn_map.get(self.difficulty)
