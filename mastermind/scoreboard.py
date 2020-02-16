#!/usr/bin/env python3

from typing import List


class Scoreboard:
    """
    Scoreboard class.
    """

    def __init__(self, num_count: int):
        """
        ScoreBoard constructor.
        """
        self.num_count = num_count
        self.player_guesses = []
        self.player_scores = []

    def generate_history(self) -> List[str]:
        """
        Generates history of guesses and scores for scoreboard.
        """
        scoreboard = []
        for i, (g, s) in enumerate(zip(self.player_guesses, self.player_scores)):
            string_builder = []
            string_builder.append(f"{i + 1}.  " if i < 9 else f"{i + 1}. ")
            string_builder.append(str([i for i in g]))
            string_builder.append("\t\t")
            correct_positions = s.get("correct_positions")
            string_builder.append("X " * correct_positions)
            correct_colors = s.get("correct_colors")
            string_builder.append("O " * correct_colors)
            string_builder.append(
                "* " * (self.num_count - int(correct_colors) - int(correct_positions)))
            scoreboard.append("".join(string_builder))
        return scoreboard

    def __str__(self) -> str:
        """
        String representation of class.
        """
        sb = self.generate_history()
        results = "\n".join([line for line in sb])
        string = "\n".join(
            ("================================================",
             "\n#   Guesses                     Scores\n",
             results,
             "\n================================================",))
        return string
