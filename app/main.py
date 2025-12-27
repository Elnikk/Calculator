import pytest

from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(2, 4) == 8

    def test_division_success(self):
        assert self.calc.division(4, 2) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(1, 2) == -1

    def teardown(self):
        print("Выполнение метода TearDown")