#!/usr/bin/python3


class Player:
    """
    Player class.
    """

    def __init__(self, name: str = "Tu", turns: int = 10):
        """
        Player constructor.
        Default value for name is Tu and default value for turns is 10.
        """
        self.name = name
        self.turns = turns
