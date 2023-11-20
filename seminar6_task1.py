class Tasks:

    def find_average(numbers: list) -> float:
        if not isinstance(numbers, list):
            raise TypeError('not list')
        if not numbers:  # len(numbers) == 0
            return 0
        return sum(numbers) / len(numbers)


class Person:
    def __init__(self, balance):
        self.balance = balance

    def transfer_money(self, bank, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError('недостаточно средств на балансе')
        self.balance -= amount
        bank.recive_money(amount)

class Bank:
    def __init__(self):
        self.balance = 0

    def recive_money(self, amount):
        self.balance += amount