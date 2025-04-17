import random
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
    print("Luo pankkitunnukset")
    käyttäjätunnus1 = input("Anna käyttäjän nimi:")
    PINkoodi1 = input("Anna Uusi PIN-koodi:")
    luottokortti_numero = random.randint(10**15, 10**16 - 1)
    print(f'Luotu luottokortti numero: FI{luottokortti_numero}')
    
    print("Kirjaudu uudelleen pankkitilille nähdääksesi tilin tilanteen.")

    yrityksiä = 0

    while yrityksiä < 3:
        käyttäjätunnus2 = input("Anna käyttäjätunnus: ")
        PINkoodi2 = input("Anna PIN-koodi: ")

        if käyttäjätunnus1 == käyttäjätunnus2 and PINkoodi1 == PINkoodi2:
            print("Oikein!")
            break
        else:
            yrityksiä = yrityksiä + 1
            print("Yritä uudelleen.")

            if yrityksiä == 3:
                print("Muisti hämärtyi!")


    heikkis_account = Account("Heikki's account", 1000.0)
    personal_account = Account("Personal account", 0.0)

    heikkis_account.withdrawal(100.0)
    personal_account.deposit(100.0)

    print(heikkis_account)
    print(personal_account)

if __name__ == "__main__":
    main()


print("This is a test message.")
# valikko
from tkinter import Tk
from dropdownmenu import ComboBoxApp

if __name__ == "__main__":
    root = Tk()
    app = ComboBoxApp(root)
    root.mainloop()