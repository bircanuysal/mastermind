#!/usr/bin/env python3

from mastermind.board import Board
from mastermind.player import Player
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
        self.player_two = None
        self.dev_mode = False

    def game_on(self):
        """
        Main entry point for game object.
        """
        self.ui.display_title()
        num_of_players = self.ui.display_home()
        if num_of_players == 1:
            self.game_single_player()
        else:
            self.game_multiplayer()

    def game_single_player(self):
        """
        Starts a single-player game.
        """
        self.player_one, self.dev_mode = self.ui.display_player_options(
            self.player_one, self.dev_mode)
        self.game_start(self.player_one)
        self.game_end()

    def game_multiplayer(self):
        """
        Starts a multiplayer game.
        """
        active_player = self.player_one
        turn = 1
        while turn <= 2:
            self.ui.display_multiplayer_instructions(turn)
            active_player, self.dev_mode = self.ui.display_player_options(
                active_player, self.dev_mode)
            self.ui.display_board_options(active_player)
            self.game_start(active_player)
            active_player = self.player_two
            turn += 1
        self.game_end()

    def game_start(self, player: Player):
        """
        Starts a new game. New board is instantiated.
        """
        self.board = Board(int(player.difficulty),
                           player.num_list, self.dev_mode)
        self.ui.display_instructions()
        timer = Timer()
        timer.start()
        victory_status = self.game_loop(player)
        timer.stop()
        print(f"The answer was {self.board.num_list}.")
        player.calculate_score(
            victory_status, timer.elapsed_time, self.board.num_count,
            len(self.board.hints_remaining))

    def game_loop(self, player: Player) -> bool:
        """
        Main loop for game. Returns true if player has won game or
        false if player has lost.
        """
        while True:
            print(f"\nGood luck, {player.name}. Have fun!")
            self.dev_mode and print(
                "Answer = " + str(self.board.num_list))
            self.board.get_player_input(player)
            self.board.check_board()
            self.board.display_history()
            if player.check_victory(self.board.num_count,
                                    self.board.history.player_scores):
                print("\nYou have won!")
                return True
            elif player.check_defeat():
                print(f"\nBetter luck next time, {player.name}!")
                return False

    def game_end(self):
        """
        End game options. Restarts the game if player chooses to play again.
        """
        play_again = self.ui.display_endgame()
        if play_again:
            self.player_one = None
            self.player_two = None
            self.dev_mode = False
            self.game_on()
