import json
from dataclasses import dataclass, field, asdict

from loader import Person


@dataclass
class PayAction:
    from_: str
    to: str
    amount: float

@dataclass
class Participant:
    name: str
    amount: float
    actions: list[PayAction] = field(default_factory=list)


@dataclass
class Calculator:
    raw_people: list[Person]
    processed_participants: list[Participant] = field(default_factory=list)
    calculated: bool = False

    # outputs
    processed_participants_output_path: str = "./output/processed_participants.json"


    def calculate(self, write_output: bool = True) -> list[Participant]:
        # create a dictionary to store the total gave amount for each expense
        total_gave_amounts= {}
        for person in self.raw_people:
            for expense in person.gave:
                if expense.name not in total_gave_amounts:
                    total_gave_amounts[expense.name] = 0
                total_gave_amounts[expense.name] += expense.amount

        # create a dictionary to store the number of people paying without exception for each expense

        num_paying_without_exception = {}
        for expense_type in total_gave_amounts.keys():
            num_paying_without_exception[expense_type] = 0
            for person in self.raw_people:
                if expense_type not in person.exceptions and not person.doesnt_pay:
                    num_paying_without_exception[expense_type] += 1

        # calculate the amount per person for each expense
        pay_chart = {}
        for expense_type, payers_count in num_paying_without_exception.items():
            pay_chart[expense_type] = total_gave_amounts[expense_type] / payers_count
        for person in self.raw_people:
            total = sum([expense.amount for expense in person.gave]) # <- sum what a person gave
            total -= sum([amount for expense, amount in pay_chart.items() if expense not in person.exceptions]) # <- minus what a person should pay that hes not excpeted of
            total -= sum([expense.amount for expense in person.took]) # <- minus what a person took
            self.processed_participants.append(Participant(name=person.name, amount=round(total,2)))

        if write_output:
            self._write_processed_participants()
        self.calculated = True
        return self.processed_participants

    def assign_pay(self) -> list[Participant]:
        if not self.calculated:
            self.calculate(False)
        router = PayRouter(self.processed_participants)
        router.route()
        self._write_processed_participants()
        return self.processed_participants

    def _write_processed_participants(self):
        with open(self.processed_participants_output_path, "w") as f:
            # f.write(json.dumps(self.processed_participants))
            json.dump([asdict(p) for p in self.processed_participants], f, indent=2)

@dataclass
class PayRouter:
    raw_participants: list[Participant]
    debt_owners: list[Participant]
    credit_owners: list[Participant]

    def __init__(self, people: list[Participant]):
        self.raw_participants = people
        self.debt_owners = [person for person in people if person.amount < 0]
        self.credit_owners = [person for person in people if person.amount >= 0]

    def route(self):
        # TODO write alg to assign pay
        # Sort the debt owners by the amount they owe
        self.debt_owners.sort(key=lambda p: p.amount, reverse=True)

        # Sort the credit owners by the amount they have
        self.credit_owners.sort(key=lambda p: p.amount, reverse=True)

        # Assign payments from the credit owners to the debt owners
        for credit_owner in self.credit_owners:
            for debt_owner in self.debt_owners:
                amount = 0
                if credit_owner.amount > 0 > debt_owner.amount:
                    amount = round(min(credit_owner.amount, abs(debt_owner.amount)),2)
                    credit_owner.amount = round(credit_owner.amount - amount,2)
                    debt_owner.amount = round(debt_owner.amount + amount,2)
                target = next((p for p in self.raw_participants if p.name == debt_owner.name), None)
                if target and amount > 0:
                    target.actions.append(PayAction(from_=debt_owner.name, to=credit_owner.name, amount=amount))