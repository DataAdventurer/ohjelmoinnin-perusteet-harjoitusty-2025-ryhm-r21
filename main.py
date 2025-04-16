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

# Pääohjelma
def main():
    heikkis_account = Account("Heikki's account", 1000.0)
    personal_account = Account("Personal account", 0.0)

    heikkis_account.withdrawal(100.0)
    personal_account.deposit(100.0)

    print(heikkis_account)
    print(personal_account)

if __name__ == "__main__":
    main()