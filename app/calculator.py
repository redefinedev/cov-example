class Calculator:
    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: int) -> int:
        return self.value + other

    def __sub__(self, other: int) -> int:
        return self.value - other

    def __eq__(self, value: object) -> bool:
        return self.value == value
