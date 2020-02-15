#!/usr/bin/env python3

from collections import Counter
from models.player import Player
from models.scoreboard import Scoreboard
from models.utils.num_validator import NumValidator
from random import randint
import requests
from typing import List


class Board:
    """
    Board class.
    """

    def __init__(self, num_count: int = 4, num_combinations: int = 7):
        """
        Board constructor.
        Default value for the amount of numbers to guess is 4. Default value
        for the number of possible number combinations is 0 through 7.
        """
        self.num_count = num_count
        self.num_combinations = num_combinations
        self.num_list = self.generate_numbers()
        self.scoreboard = Scoreboard(self.num_count)

    def generate_numbers(self) -> List[int]:
        """
        Generates random numbers using the random.org API. If for any reason
        that call is unsuccessful, the random libary is used as backup.
        """
        url = "https://www.random.org/integers/"
        query_string = {"num": "4", "min": "0", "max": str(self.num_combinations),
                        "col": "1", "base": "10", "format": "plain",
                        "rnd": "new"}
        print("Generating board...")
        response = requests.request("GET", url, params=query_string)
        if response.status_code == 200:
            return [int(n) for n in response.text.split("\n") if len(n)]
        else:
            return [randint(0, self.num_combinations)
                    for i in range(self.num_count)]

    def display(self):
        """
        Displays the current status of the board. This includes a list of
        the player's previous guesses as well as the player's current score.
        """
        print(self.scoreboard)
        self.display_legend()

    def get_player_input(self, player: Player):
        """
        Ask current player for input. Will only accept valid integers.
        """
        guesses = []
        guess_count = 1
        nv = NumValidator()
        print(f"\n{player.turns} turns left.")
        print(f"Please enter a number between 0 and {self.num_combinations}.")
        while len(guesses) != self.num_count:
            guess = nv.get_guess(
                guess_count, 0, self.num_combinations)
            guesses.append(guess)
            guess_count += 1
        player.turns -= 1
        self.scoreboard.player_guesses.append(guesses)

    def check_board(self):
        """
        Validates user input with correct numbers.
        Algorithm speed is currently O(n) time complexity and O(n) space
        complexity.
        """
        last_guesses = self.scoreboard.player_guesses[-1]
        correct_colors = sum(
            (Counter(self.num_list) & Counter(last_guesses)).values())
        correct_positions = 0
        for i in range(len(last_guesses)):
            if last_guesses[i] == self.num_list[i]:
                correct_positions += 1
                correct_colors -= 1
        self.scoreboard.player_scores.append(
            {"correct_colors": correct_colors, "correct_positions": correct_positions})

    def display_legend(self):
        """
        Displays the board legend.
        """
        print("\nX = Correct number, correct location\n"
              "O = Correct number, incorrect location\n"
              "* = Incorrect number, incorrect location")
