#r21
#Maripuu Kristofer, Petter Paananen, Perälä Aapeli
import random
from pankkitili import Account

def main():
    print("Luo pankkitunnukset")
    käyttäjätunnus1 = input("Anna käyttäjän nimi: ")
    PINkoodi1 = input("Anna Uusi PIN-koodi: ")
    luottokortti_numero = random.randint(10**15, 10**16 - 1)
    print(f'Luotu luottokortti numero: FI{luottokortti_numero}')

    print("Kirjaudu uudelleen pankkitilille nähdääksesi tilin tilanteen.")
    yrityksiä = 0

    while yrityksiä < 3:
        käyttäjätunnus2 = input("Anna käyttäjätunnus: ")
        PINkoodi2 = input("Anna PIN-koodi: ")

        if käyttäjätunnus1 == käyttäjätunnus2 and PINkoodi1 == PINkoodi2:
            print("Oikein! Kirjautuminen onnistui.")
            oma_tili = Account("Personal account", 10000.0)
            break
        else:
            yrityksiä += 1
            print("Yritä uudelleen.")
            if yrityksiä == 3:
                print("Muisti hämärtyi!")
                return  

    heikkis_account = Account("Heikki's account", 1000.0)
    personal_account = oma_tili 

    heikkis_account.withdrawal(100.0)
    personal_account.deposit(100.0)

    print(heikkis_account)
    print(personal_account)

main()