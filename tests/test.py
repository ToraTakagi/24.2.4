import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_division_success(self):
        assert self.calculator.division(self, 4, 2) == 2

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 10, 5) == 5

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 2, 2) == 4

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')