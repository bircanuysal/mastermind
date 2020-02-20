#!/usr/bin/env python3

import getpass
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
        print("======================================================"
              "\n\nMASTERMIND\n\n"
              "======================================================\n"
              "Test your code-cracking prowess with Mastermind,\n"
              "the challenging game of logic and deduction.\n"
              "======================================================\n")

    def display_home(self) -> int:
        """
        Displays home screen with options for single-player, multiplayer or
        viewing the leaderboard.
        """
        while True:
            print("Welcome!\n"
                  "1. Single-player\n"
                  "2. Multi-player\n"
                  "3. View leaderboard\n")
            option = self.nv.get_home_screen(1, 3)
            if option == 1:
                return 1
            elif option == 2:
                return 2
            else:
                Leaderboard.display_leaderboard()

    def display_player_options(self, player: Player, dev_mode: bool) -> Player:
        """
        Displays player options and returns a new instance of a Player.
        """
        name = self.sv.get_name()
        if name == "Tu":
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

    def display_board_options(self, player: Player):
        """
        Displays prompt for assigning board numbers to a player.
        """
        max_n = 9 if int(player.difficulty) == 4 else 7
        while True:
            numbers = getpass.getpass(
                f"\nCodemaker, enter in four numbers between 0 and {max_n}: ")
            try:
                num_list = list(numbers)
                if len(num_list) != 4:
                    raise ValueError
                num_list = [int(i) for i in num_list]
                if any(i > max_n for i in num_list):
                    raise ValueError
                player.num_list = num_list
                return
            except Exception:
                print("Invalid entry. Try again.")

    def display_instructions(self):
        """
        Displays game instructions.
        """
        print("\n======================================================\n"
              "Try to guess the correct number sequence by\n"
              "entering four numbers.\n"
              "======================================================")

    def display_multiplayer_instructions(self, active: int):
        """
        Displays game instructions for multiplayer mode.
        """
        n = "first" if active == 1 else "second"
        opposite = 2 if active == 1 else 1
        print("\n======================================================\n"
              f"\nIn the {n} round, Player {active} will be the Codebreaker\n"
              f"and attempts to guess while Player {opposite} will be the\n"
              "Codemaker and creates the sequence of numbers.\n\n"
              "======================================================\n")

    def display_endgame(self):
        """
        Displays end game options. Users can play again, view leaderboard
        or quit.
        """
        while True:
            print("What would you like to do next?\n"
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
