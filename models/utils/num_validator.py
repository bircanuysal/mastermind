from models.utils.validator import Validator


class NumValidator(Validator):
    """
    Number validator class.
    """

    def get_difficulty(self, min_value: int, max_value: int) -> str:
        """
        Gets user input for difficulty.
        """
        prompt = "Select your difficulty: "
        return str(self.get_input(prompt, min_value, max_value))

    def get_guess(self, guess_count: int, min_value: int, max_value: int) -> str:
        """
        Gets user input for guesses.
        """
        prompt = "Enter in your guess for position " + str(guess_count) + " : "
        return self.get_input(prompt, min_value, max_value)

    def get_input(self, prompt: str, min_value: int, max_value) -> int:
        """
        Validates user input is in accepted number range or will re-prompt user
        to re-enter.
        """
        while True:
            num = input(prompt).strip()
            try:
                num = int(num)
                if num < min_value or num > max_value:
                    raise Exception
                return num
            except Exception:
                print(
                    f"Invalid input. Please enter in a number from {min_value} to {max_value}.")
