#!/usr/bin/env python3
# Reset leaderboard with default leaderboard

import os

if __name__ == "__main__":
    try:
        os.system(
            "cp ./leaderboard_default.json ./leaderboard.json")
    except Exception as e:
        print(f"Error:\n{e}")
