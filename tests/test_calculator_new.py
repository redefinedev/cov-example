import pytest

from app.calculator import Calculator

class TestCalculator:
    @pytest.fixture()
    def calculator(self):
        return Calculator(10)

    def test_mul(self, calculator):
        assert calculator * 2 == 20

        # Test that multiplication is immutable
        assert calculator * 3 == 30

        # Test that multiplication by 0 works
        assert calculator * 0 == 0

        # Test rmul
        assert 2 * calculator == 20

    def test_div(self, calculator):
        assert calculator / 2 == 5

        # Test that multiplication is immutable
        assert calculator / 2 == 5

        # Test that multiplication by 0 works
        with pytest.raises(ZeroDivisionError):
            calculator / 0

        # Test rtruediv
        assert 100 / calculator == 10
