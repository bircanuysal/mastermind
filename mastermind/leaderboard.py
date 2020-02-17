#!/usr/bin/env python3

import json
from typing import List, Dict


class Leaderboard:
    """
    Leaderboard class.
    """

    file_path = "data/leaderboard.json"

    @classmethod
    def open_leaderboard(cls) -> List[Dict[str, str]] or None:
        """
        Attempts to open leaderboard. Returns leaderboard if successful.
        """
        try:
            with open(cls.file_path) as f:
                data = json.load(f)
                return data
        except (IOError, Exception):
            print("Could not load leaderboard at this time.")
            return None

    @classmethod
    def display_leaderboard(cls):
        """
        Displays current leaderboard, sorted in descending order.
        """
        data = cls.open_leaderboard()
        if data:
            sorted_by_score = sorted(
                data, key=lambda e: int(e.get("score")), reverse=True)
            name, score = "Name", "High Score"
            print(f"\n{name: <30} {score: >17}\n"
                  "================================================")
            for entry in sorted_by_score:
                entry_name = entry.get("name")
                entry_score = entry.get("score")
                print(f"{entry_name: <30} {entry_score: >17}")
            print("================================================\n")

    @classmethod
    def write_score(cls, name: str, score: int):
        """
        Writes name and score to leaderboard.
        """
        data = cls.open_leaderboard()
        if data:
            new_entry = {"name": name,
                         "score": str(score)}
            data.append(new_entry)
            try:
                with open(Leaderboard.file_path, 'w') as f:
                    json.dump(data, f)
            except (IOError, Exception):
                print("Could not write score to leaderboard at this time.")
