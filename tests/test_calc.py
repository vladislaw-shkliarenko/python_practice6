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

def test_multiply_positive():
    calc = Calculator(3, 7)
    assert calc.multiply() == 21

def test_multiply_by_zero():
    calc = Calculator(5, 0)
    assert calc.multiply() == 0
    
def test_divide_positive():
    calc = Calculator(10, 2)
    assert calc.divide() == 5

def test_divide_by_zero():
    calc = Calculator(10, 0)
    assert calc.divide() == "Ділення на 0 неможливе"

def test_power_positive():
    calc = Calculator(2, 3)
    assert calc.power() == 8

def test_power_negative():
    calc = Calculator(-2, 3)
    assert calc.power() == -8

def test_random_positive():
    num = Calculator.random_number(1, 10)
    assert 1 <= num <= 10

def test_random_negative():
    num = Calculator.random_number(10, 5)
    assert num is None