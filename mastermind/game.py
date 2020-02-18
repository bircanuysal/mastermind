#!/usr/bin/env python3

from mastermind.board import Board
from mastermind.user_interface import UserInterface
from mastermind.utils.timer import Timer


class Game:
    """
    Game class.
    """

    def __init__(self):
        """
        Game constructor.
        """
        self.ui = UserInterface()
        self.board = None
        self.player_one = None
        self.developer_mode = False

    def game_on(self):
        """
        Main entry point for game object.
        """
        self.ui.display_title()
        self.ui.display_home()
        self.player_one, self.developer_mode = self.ui.display_player_options(
            self.player_one, self.developer_mode)
        self.game_start()

    def game_start(self):
        """
        Starts a new game. New board is instantiated.
        """
        if self.player_one.difficulty == "4":
            self.board = Board(9, self.developer_mode)
        else:
            self.board = Board(7, self.developer_mode)
        self.ui.display_instructions()
        timer = Timer()
        timer.start()
        victory_status = self.game_loop()
        timer.stop()
        print(f"The answer was {self.board.num_list}.")
        self.player_one.calculate_score(
            victory_status, timer.elapsed_time, self.board.num_count,
            len(self.board.hints_remaining))
        self.game_end()

    def game_loop(self) -> bool:
        """
        Main loop for game. Returns true if player has won game or
        false if player has lost.
        """
        while True:
            print(f"\nGood luck, { self.player_one.name}. Have fun!")
            self.developer_mode and print(
                "Answer = " + str(self.board.num_list))
            self.board.get_player_input(self.player_one)
            self.board.check_board()
            self.board.display_history()
            if self.player_one.check_victory(self.board.num_count,
                                             self.board.history.player_scores):
                print("\nYou have won!")
                return True
            elif self.player_one.check_defeat():
                print(f"\nBetter luck next time, {self.player_one.name}!")
                return False

    def game_end(self):
        """
        End game options. Restarts the game if player chooses to play again.
        """
        play_again = self.ui.display_endgame()
        if play_again:
            self.ui.display_player_options(
                self.player_one, self.developer_mode)
            self.game_start()
