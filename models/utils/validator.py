#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Validator(ABC):
    """
    Validator abstract class.
    """

    @abstractmethod
    def get_input(self):
        """
        Method to get user input.
        """
        pass
