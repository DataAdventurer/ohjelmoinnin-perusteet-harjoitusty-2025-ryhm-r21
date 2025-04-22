#r21
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"{self.name}: {self.balance:.2f} €"
