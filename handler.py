from typing import Union
from calculator import Calculator
from loader import Loader

def handler(payload: Union[str, dict, list]):
    loader = Loader(raw_people=payload)
    people = loader.load()
    calculator = Calculator(people)
    return calculator.assign_pay()
