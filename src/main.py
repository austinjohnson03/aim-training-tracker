from scenario import Scenario
from challenge import Challenge
from menu import Menu

from datetime import date, time

def main() -> None:
    pass


def create_scenario(name: str) -> Scenario:
    return Scenario(name)

def create_challenge(scenario: Scenario, idx: int, score: float, accuracy: float) -> Challenge:

    score = float(input(f"Enter the score for '{scenario}': "))

    current_date = date.now()
    current_time = time.now()

