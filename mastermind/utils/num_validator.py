#!/usr/bin/env python3

from mastermind.utils.validator import Validator


class NumValidator(Validator):
    """
    Number validator class.
    """

    def get_home_screen(self, min_value: int, max_value: int) -> int:
        """
        Gets user input for home screen.
        """
        prompt = "What would you like to do? "
        return self.get_input(prompt, min_value, max_value)

    def get_difficulty(self, min_value: int, max_value: int) -> int:
        """
        Gets user input for difficulty.
        """
        prompt = "Select your difficulty: "
        return self.get_input(prompt, min_value, max_value)

    def get_guess(self, guess_count: int, min_value: int, max_value: int) -> int:
        """
        Gets user input for guesses.
        """
        prompt = f"Enter in your guess for position {str(guess_count)}: "
        return self.get_input(prompt, min_value, max_value, True)

    def get_endgame(self, min_value: int, max_value: int) -> int:
        """
        Gets user input for endgame options.
        """
        prompt = "Select an option: "
        return self.get_input(prompt, min_value, max_value)

    def get_input(self, prompt: str, min_value: int, max_value,
                  allow_hints: bool = False) -> int:
        """
        Validates user input is in accepted number range or will re-prompt user
        to re-enter. Returns -1 if hints are allowed and user enters in 'h'.
        """
        while True:
            num = input(prompt).strip()
            try:
                if allow_hints and num == "h":
                    return -1
                num = int(num)
                if num < min_value or num > max_value:
                    raise Exception
                return num
            except Exception:
                print(
                    f"Invalid input. Please enter in a number from {min_value}"
                    f" to {max_value}.")
