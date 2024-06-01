class Calculator:
    def __init__(self, value: int) -> None:
        self.value = value

    def __add__(self, other: int) -> int:
        return self.value + other

    def __sub__(self, other: int) -> int:
        return self.value - other

    def __eq__(self, value: object) -> bool:
        return self.value == value

    def __mul__(self, other: int) -> int:
        return self.value * other

    def __rmul__(self, other: int) -> int:
        return self.value * other

    def __truediv__(self, other: int) -> int:
        return self.value / other

    def __rtruediv__(self, other: int) -> int:
        return other / self.value
