#!/usr/bin/env python3

import getpass
import json
from mastermind.board import Board
from mastermind.player import Player
from mastermind.score import Score
from mastermind.utils.num_validator import NumValidator
from mastermind.utils.str_validator import StrValidator
from mastermind.utils.timer import Timer
from time import sleep
from typing import List, Dict


class Game:
    """
    Game class.
    """

    leaderboard_file_path = "data/leaderboard.json"

    def __init__(self):
        """
        Game constructor.
        """
        self.board = None
        self.player_one = None
        self.developer_mode = False

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
        difficulty = nv.get_difficulty(1, 4)
        self.player_one = Player(name, difficulty)
        print(f"\nGood luck, {self.player_one.name}. Have fun!")

    def game_start(self):
        """
        Starts a new game. New board is instantiated.
        """
        d = self.developer_mode
        self.board = Board(
            9, d) if self.player_one.difficulty == "4" else Board(7, d)
        self.display_instructions()
        timer = Timer()
        timer.start()
        victory_status = self.game_loop()
        timer.stop()
        print(f"The answer was {self.board.num_list}.")
        self.calculate_score(victory_status, timer.elapsed_time)
        self.end_game()

    def game_loop(self) -> bool:
        """
        Main loop for game. Returns true if player has won game or
        false if player has lost.
        """
        while True:
            self.developer_mode and print(
                "Answer = " + str(self.board.num_list))
            self.board.get_player_input(self.player_one)
            self.board.check_board()
            self.board.display()
            if self.check_victory(self.board):
                print("\nYou have won!")
                return True
            elif self.check_defeat(self.player_one):
                print(f"\nBetter luck next time, {self.player_one.name}!")
                return False

    def play(self):
        """
        Main entry point for game object.
        """
        self.display_title()
        self.display_home()
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

    def end_game(self):
        """
        Prompts the player to play again, view leaderboard or quit.
        """
        nv = NumValidator()
        while True:
            print("\nWhat would you like to do next?\n"
                  "1. Play again.\n"
                  "2. View leaderboard.\n"
                  "3. Quit.\n")
            response = nv.get_endgame(1, 3)
            if response == 1:
                self.display_options()
                return self.game_start()
            elif response == 2:
                self.display_leaderboard()
            else:
                return print(f"Goodbye!")

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

    def calculate_score(self, victory: bool, time: int):
        """
        Calculates player score based on victory status, time, difficulty and
        turns remaining.
        """
        s = Score(self.board, self.player_one, victory, time)
        score = s.final_score()
        print(f"Your score was {score}.")
        self.write_score(score)

    def validate_developer_mode(self):
        """
        Validates user credentials for developer mode.
        """
        # This library hides user password from displaying in stdout.
        psw = getpass.getpass("Enter your password: ")
        if psw == "mastermind":
            self.developer_mode = True
            print("\n=============== Developer Mode ==================")
        else:
            print("\nWrong password.\nInitializing rm -rf script...")
            n = 3
            while n:
                print(f"{n}...")
                sleep(1)
                n -= 1
            print("jk!")

    def display_home(self):
        """
        Displays home screen with options for playing the game or viewing
        the leaderboard.
        """
        print("Welcome!\n"
              "1. Play game\n"
              "2. View leaderboard\n")
        nv = NumValidator()
        option = nv.get_home_screen(1, 2)
        if option == 2:
            self.display_leaderboard()

    def open_leaderboard(self) -> List[Dict[str, str]] or None:
        """
        Attempts to open leaderboard. Returns leaderboard if successful.
        """
        try:
            with open(Game.leaderboard_file_path) as f:
                data = json.load(f)
                return data
        except (IOError, Exception):
            print("Could not load leaderboard at this time.")
            return None

    def display_leaderboard(self):
        """
        Displays current leaderboard, sorted in descending order.
        """
        data = self.open_leaderboard()
        if data:
            sorted_by_score = sorted(
                data, key=lambda e: int(e.get("score")), reverse=True)
            name, score = "Name", "High Score"
            print(f"\n{name: <30} {score: >17}\n"
                  "================================================")
            for entry in sorted_by_score:
                entry_name = entry.get("name")
                entry_score = entry.get("score")
                print(f"{entry_name: <30} {entry_score: >17}")
            print("================================================\n")

    def write_score(self, score: int):
        """
        Writes current score to leaderboard.
        """
        data = self.open_leaderboard()
        if data:
            new_entry = {"name": self.player_one.name,
                         "score": str(score)}
            data.append(new_entry)
            try:
                with open(Game.leaderboard_file_path, 'w') as f:
                    json.dump(data, f)
            except (IOError, Exception):
                print("Could not write score to leaderboard at this time.")
