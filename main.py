import uvicorn

from app import app
from calculator import Calculator
from loader import Loader
from printer import print_data

def main():
    loader = Loader(path='./data/debt.json')
    people = loader.load()
    calculator = Calculator(people)
    output = calculator.assign_pay()
    return output


if __name__ == '__main__':
    # uvicorn.run(app, host="0.0.0.0", port=8080)

    output = main()
    print_data(output)
