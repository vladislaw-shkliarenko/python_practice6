import pytest
from app.calculator import Calculator

def test_add_positive():
    calc = Calculator(5, 10)
    assert calc.add() == 15

def test_add_negative():
    calc = Calculator(-5, -10)
    assert calc.add() == -15

def test_subtract_positive():
    calc = Calculator(10, 5)
    assert calc.subtract() == 5

def test_subtract_negative():
    calc = Calculator(5, 10)
    assert calc.subtract() == -5