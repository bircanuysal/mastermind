#!/usr/bin/python3

from collections import Counter
from models.player import Player
from random import randint
from typing import List


class Board:
    """
    Board class.
    """

    def __init__(self, num_count: int = 4, num_combinations: int = 7):
        """
        Board constructor.
        Default value for the amount of numbers to guess is 4. Default value
        for the number of possible number combinations is 7.
        """
        self.num_count = num_count
        self.num_combinations = num_combinations
        self.num_list = self.generate_numbers()
        self.player_guesses = []
        self.player_scores = []
        print("Answer = " + str(self.num_list))

    def generate_numbers(self) -> List[int]:
        """
        Generates random numbers using the random libary.
        """
        return ([randint(0, self.num_combinations)
                 for i in range(self.num_count)])

    def display(self):
        """
        Displays the current status of the board. This includes a list of
        the player's previous guesses as well as the player's current score.
        """
        print(f"=== Board ===")
        self.player_guesses and print(
            f"=== Player guesses {self.player_guesses}")
        self.player_scores and print(
            f"=== Player score {self.player_scores} ===")

    def get_player_input(self, player: Player):
        """
        Ask current player for input. Will only accept valid integers.
        """
        guesses = []
        guess_count = 1
        while len(guesses) != self.num_count:
            guess = input(f"Enter in your guess for position {guess_count}: ")
            # TODO
            # Validate user input
            guesses.append(int(guess))
            guess_count += 1
        self.player_guesses.append(guesses)
        player.turns -= 1

    def check_board(self):
        """
        Validates user input with correct numbers.
        Algorithm speed is currently O(n) time complexity and O(n) space
        complexity.
        """
        last_guesses = self.player_guesses[-1]
        correct_colors = (len(Counter(self.num_list)
                              & Counter((last_guesses))))
        correct_positions = 0
        for i in range(len(last_guesses)):
            if last_guesses[i] == self.num_list[i]:
                correct_positions += 1
                correct_colors -= 1
        self.player_scores.append(
            {"correct_colors": correct_colors,
             "correct_positions": correct_positions})
