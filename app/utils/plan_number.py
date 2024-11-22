class SingletonMeta(type):
    """
    A metaclass that creates a Singleton base class when called.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PlanNumber(metaclass=SingletonMeta):
    def __init__(self, initial_number: int = 7):
        self._number = initial_number

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, value: int):
        self._number = value

    def increment(self):
        self._number += 1

    def __str__(self):
        return f"PlanNumber: {self._number}"
