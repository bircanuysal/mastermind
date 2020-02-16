#!/usr/bin/env python3

import time


class TimerError(Exception):
    """
    A custom exception used to report errors in Timer class.
    """


class Timer:
    """
    Timer class.
    """

    def __init__(self):
        """
        Timer constructor.
        """
        self.start_time = None
        self.elapsed_time = None

    def start(self):
        """
        Starts a new timer.
        """
        if self.start_time:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self.start_time = time.perf_counter()

    def stop(self):
        """
        Stops the timer, and reports the elapsed time.
        """
        if not self.start_time:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        self.elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
        print(f"Elapsed time: {self.elapsed_time:0.2f} seconds.")
