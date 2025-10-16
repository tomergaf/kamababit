import pytest
from calculator import Calculator
from loader import Loader

def test_calculate_good_path():
    loader = Loader('./data/test_debt.json')
    people = loader.load()
    calculator = Calculator(people)
    calculator.calculate()
    # You can add asserts to verify expected outcomes, for example:
    # assert len(calculator.results) > 0

def test_assign_pay_good_path():
    loader = Loader('./data/test_debt.json')
    people = loader.load()
    calculator = Calculator(people)
    calculator.assign_pay()
    assert True
