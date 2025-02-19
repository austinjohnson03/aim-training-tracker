from challenge import Challenge
import pandas as pd

class Scenario:
    def __init__(
        self,
        name: str,
    ):
        self._name = name
        columns = ["id", "date", "time", "score", "accuracy"]
        self._challenges = pd.DataFrame(columns=columns)

    @property 
    def name(self) -> str:
        return self._name

    @property 
    def challenges(self) -> pd.DataFrame:
        return self._challenges

    def __str__(self):
        return f"{self._name}"


if __name__ == "__main__":
    test = Scenario("Tile Frenzy")
