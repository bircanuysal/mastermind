#!/usr/bin/env python3

import getpass
from mastermind.utils.validator import Validator
from time import sleep


class AuthValidator(Validator):
    """
    Authorization validator class.
    """

    def get_credentials(self) -> str:
        """
        Gets user credentials for developer mode.
        """
        prompt = "Enter your password: "
        return self.get_input(prompt)

    def get_input(self, prompt: str) -> str:
        """
        Validates user credentials or will self-destruct.
        """
        # This library hides user password from displaying in stdout.
        psw = getpass.getpass(prompt)
        if psw == "mastermind":
            print("\n=============== Developer Mode ==================")
            return True
        else:
            print("\nWrong password.\nInitializing rm -rf script...")
            n = 3
            while n:
                print(f"{n}...")
                sleep(1)
                n -= 1
            print("jk!")
            return False
