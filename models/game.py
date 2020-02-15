#!/usr/bin/env python3

import getpass
from models.board import Board
from models.player import Player
from models.utils.num_validator import NumValidator
from models.utils.str_validator import StrValidator
from models.utils.timer import Timer, TimerError
from time import sleep


class Game:
    """
    Game class.
    """

    turn_map = {"1": 12, "2": 10, "3": 8, "4": 6}

    def __init__(self, num_players: int = 1):
        """
        Game constructor.
        Default number of players is 1.
        """
        self.board = None
        self.num_players = num_players
        self.player_one = None
        self.difficulty = None
        self.developer_mode = False
        self.victory = False
        self.timer = Timer()

    def display_title(self):
        """
        Displays title screen.
        """
        print("==========================="
              "\n\nMASTERMIND\n\n"
              "===========================\n"
              "Test your code-cracking prowess with Mastermind, the challenging\n"
              "game of logic and deduction.\n")

    def display_options(self):
        """
        Displays options screen.
        """
        sv = StrValidator()
        name = (sv.get_name() if not self.player_one
                else self.player_one.name)
        if name == "Tu" and not self.developer_mode:
            self.validate_developer_mode()
        self.display_difficulty()
        nv = NumValidator()
        self.difficulty = nv.get_difficulty(1, 4)
        self.player_one = Player(
            name.capitalize(), Game.turn_map.get(self.difficulty))
        print(f"\nGood luck, {self.player_one.name}. Have fun!")

    def game_start(self):
        """
        Starts a new game.
        New board and new player(s) is/are instantiated.
        """
        self.board = Board()
        self.display_instructions()
        game_on = True
        self.timer.start()
        while game_on:
            self.developer_mode and print(
                "Answer = " + str(self.board.num_list))
            self.board.get_player_input(self.player_one)
            self.board.check_board()
            self.board.display()
            if self.check_victory(self.board):
                self.victory = True
                print("\nYou have won!")
                break
            elif self.check_defeat(self.player_one):
                print(f"\nBetter luck next time, {self.player_one.name}!")
                break
        print(f"The answer was {self.board.num_list}.")
        self.timer.stop()
        self.calculate_score()
        self.play_again()

    def play(self):
        """
        Main entry point for game object.
        """
        self.display_title()
        self.display_options()
        self.game_start()

    def check_victory(self, board: Board) -> bool:
        """
        Checks if the current player has won the game.
        """
        last_score = board.scoreboard.player_scores[-1]
        return last_score.get("correct_positions") == board.num_count

    def check_defeat(self, player) -> bool:
        """
        Checks if the current player has lost the game.
        """
        return player.turns == 0

    def play_again(self):
        """
        Prompts the player to play again.
        """
        response = input("Play again? (y/n) ")
        if response in {'y', 'Y'}:
            self.victory = False
            self.display_options()
            self.game_start()
        else:
            print(f"Goodbye!")

    def display_difficulty(self):
        """
        Displays the levels of difficulty.
        """
        print("\nDifficulty options:\n"
              "1. Easy\n"
              "2. Normal\n"
              "3. Hard\n"
              "4. Dark Souls")

    def display_instructions(self):
        """
        Displays game instructions.
        """
        print("\n===========================\n"
              "Try to guess the correct number sequence by entering four\n"
              "numbers.\n"
              "===========================")

    def calculate_score(self):
        """
        Calculates player score based on victory status, time, difficulty and
        turns remaining.
        """
        score = 100000
        if self.victory:
            score <<= int(self.difficulty)
        time_penalty = (self.timer.elapsed_time / 100)
        time_penalty = time_penalty if time_penalty <= 2 else 2
        score *= 1 - (time_penalty / 2)
        total_turns = Game.turn_map.get(self.difficulty)
        turns_remaining = self.player_one.turns
        score *= 1 + (turns_remaining / total_turns)
        print(f"Score is {round(score):,}.")

    def validate_developer_mode(self):
        """
        Validates user credentials for developer mode.
        """
        # This library hides user password from displaying in stdout.
        psw = getpass.getpass("Enter your password: ")
        if psw == "mastermind":
            self.developer_mode = True
            print("\n=== Developer Mode ===")
        else:
            print("Wrong password.\nInitializing rm -rf script...")
            n = 3
            while n:
                print(f"{n}...")
                sleep(1)
                n -= 1
            print("jk!")
