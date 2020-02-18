#!/usr/bin/env python3

from mastermind.leaderboard import Leaderboard
from mastermind.player import Player
from mastermind.utils.auth_validator import AuthValidator
from mastermind.utils.num_validator import NumValidator
from mastermind.utils.str_validator import StrValidator


class UserInterface:
    """
    User interface class.
    """

    def __init__(self):
        """
        User Interface constructor. Initializes all validators as instance
        attributes.
        """
        self.nv = NumValidator()
        self.sv = StrValidator()
        self.av = AuthValidator()

    def display_title(self):
        """
        Displays title screen.
        """
        print("================================================"
              "\n\nMASTERMIND\n\n"
              "================================================\n"
              "Test your code-cracking prowess with Mastermind,\n"
              "the challenging game of logic and deduction.\n"
              "================================================\n")

    def display_home(self):
        """
        Displays home screen with options for playing the game or viewing
        the leaderboard.
        """
        print("Welcome!\n"
              "1. Play game\n"
              "2. View leaderboard\n")
        option = self.nv.get_home_screen(1, 2)
        if option == 2:
            Leaderboard.display_leaderboard()

    def display_player_options(self, player: Player, dev_mode: bool) -> Player:
        """
        Displays player options and returns a new instance of a Player.
        """
        name = (self.sv.get_name() if not player
                else player.name)
        if name == "Tu" and not dev_mode:
            dev_mode = self.av.get_credentials()
        self.display_difficulty()
        difficulty = self.nv.get_difficulty(1, 4)
        return (Player(name, str(difficulty)), dev_mode)

    def display_difficulty(self):
        """
        Displays the levels of difficulty.
        """
        print("\nDifficulty options:\n"
              "1. Easy - 12 turns.\n"
              "2. Normal - 10 turns.\n"
              "3. Hard - 8 turns.\n"
              "4. Dark Souls - 6 turns. 10 numbers to choose from.\n")

    def display_instructions(self):
        """
        Displays game instructions.
        """
        print("\n================================================\n"
              "Try to guess the correct number sequence by\n"
              "entering four numbers.\n"
              "================================================")

    def display_endgame(self):
        """
        Displays end game options. Users can play again, view leaderboard
        or quit.
        """
        while True:
            print("\nWhat would you like to do next?\n"
                  "1. Play again.\n"
                  "2. View leaderboard.\n"
                  "3. Quit.\n")
            response = self.nv.get_endgame(1, 3)
            if response == 1:
                return True
            elif response == 2:
                Leaderboard.display_leaderboard()
            else:
                print("Goodbye!")
                return False
