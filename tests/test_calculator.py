import pytest

from app.calculator import Calculator

class TestCalculator:
    @pytest.fixture()
    def calculator(self):
        return Calculator(0)

    def test_initial_value(self, calculator):
        assert calculator == 0

    def test_add(self, calculator):
        assert calculator + 1 == 1

        # Test that addition is immutable
        assert calculator + 2 == 2

    def test_sub(self, calculator):
        assert calculator - 1 == -1

        # Test that subtraction is immutable
        assert calculator - 2 == -2
