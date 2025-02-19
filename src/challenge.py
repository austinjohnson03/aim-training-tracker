from datetime import date, time 

class Challenge:
    def __init__(
        self,
        idx: int,
        date: date,
        time: time,
        score: float,
        accuracy: float
    ):
        self._idx = idx
        self._date = date
        self._time = time 
        self._score = score
        self._accuracy = accuracy

    @property 
    def idx(self) -> int:
        return self._idx 

    @idx.setter
    def idx(self, value:int) -> None:
        if isinstance(value, int):
            self._idx = value
        else:
            raise ValueError

    @property
    def date(self) -> date:
        return self._date

    @date.setter
    def date(self, value: date) -> None:
        if isinstance(value, date):
            self._date = value
        else:
            raise ValueError

    @property 
    def time(self) -> time:
        return self._time 

    @time.setter
    def time(self, value: time) -> None:
        if isinstance(value, time):
            self._time = value
        else:
            raise ValueError

    @property 
    def score(self) -> float:
        return self._score

    @score.setter 
    def score(self, value: float) -> None:
        if isinstance(value, float):
            self._score = value 
        else:
            raise ValueError

    @property 
    def accuracy(self) -> float:
        return self._float 

    @accuracy.setter
    def accuracy(self, value: float) -> None:
        if isinstance(value, float):
            self._accuracy = value
        else:
            raise ValueError

    def __str__(self) -> str:
        return f"ID: {self._idx}\nDatetime: {self._date} {self._time}\nScore: {self._score}\nAccuracy: {self._accuracy * 100}%"


if __name__ == "__main__":
    test = Challenge(1, date(2025, 2, 18), time(21,59,00), 234034.12, 0.95)

    print(test)

