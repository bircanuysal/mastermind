#!/usr/bin/python3

from models.board import Board
from models.player import Player
from models.utils.num_validator import NumValidator


class Game:
    """
    Game class.
    """

    def __init__(self, num_players: int = 1):
        """
        Game constructor.
        Default number of players is 1.
        """
        self.board = None
        self.num_players = num_players
        self.player_one = None
        self.developer_mode = False

    def display_title(self):
        """
        Displays title screen.
        """
        print("==========================="
              "\n\nMASTERMIND\n\n"
              "===========================")

    def display_options(self):
        """
        Displays options screen.
        """
        name = (input(
            "What is your name? ") if not self.player_one
            else self.player_one.name)
        self.display_difficulty()
        nv = NumValidator()
        difficulty = nv.get_difficulty(0, 4)
        if difficulty == "0":
            self.developer_mode = True
            print("<-- Developer Mode -->")
        turn_map = {"0": 3, "1": 12, "2": 10, "10": 8, "4": 6}
        self.player_one = Player(name.capitalize(), turn_map.get(difficulty))
        print(f"Good luck, {self.player_one.name}. Have fun!")

    def game_start(self):
        """
        Starts a new game.
        New board and new player(s) is/are instantiated.
        """
        self.board = Board()
        game_on = True
        while game_on:
            self.developer_mode and print(
                "Answer = " + str(self.board.num_list))
            self.board.get_player_input(self.player_one)
            self.board.check_board()
            self.board.display()
            if self.check_victory(self.board):
                print("You have won!")
                break
            if self.check_defeat(self.player_one):
                print(f"Better luck next time, {self.player_one.name}!")
                print(f"The answer was {self.board.num_list}")
                break
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
            self.developer_mode = False
            self.display_options()
            self.game_start()
        else:
            print(f"Goodbye!")

    def display_difficulty(self):
        """
        Displays the levels of difficulty.
        There is a secret "d" option for developer mode.
        """
        print("Difficulty options:\n"
              "1. Easy\n"
              "2. Normal\n"
              "3. Hard\n"
              "4. Dark Souls")
