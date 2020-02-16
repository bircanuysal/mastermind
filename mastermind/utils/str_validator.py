#!/usr/bin/env python3

from mastermind.utils.validator import Validator


class StrValidator(Validator):
    """
    String validator class.
    """

    def get_name(self) -> str:
        """
        Gets user input for names.
        """
        prompt = "What is your name? "
        return self.capitalize(self.get_input(prompt))

    def get_input(self, prompt: str) -> str:
        """
        Validates user input to contain only alphabet characters or spaces
        or will re-prompt user to re-enter.
        """
        while True:
            string = input(prompt).strip()
            if self.is_alpha_or_space(string):
                return string
            else:
                print("Invalid input. Only alphabet characters and spaces only.")

    def is_alpha_or_space(self, string: str) -> bool:
        """
        Determines if given string has only alphabet characters or spaces.
        """
        for c in list(string):
            if c == " ":
                continue
            if not c.isalpha():
                return False
        return True

    def capitalize(self, string: str) -> str:
        """
        Capitalize all words of a string.
        """
        return " ".join([word.capitalize() for word in string.split()])
