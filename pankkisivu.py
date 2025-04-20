import tkinter as tk
from tkinter import messagebox
from pankkitili import Account

tili = Account("Käyttäjä", 500.0)
root = tk.Tk()
root.title("Pankkisovellus")
root.geometry("300x250")

def näytä_saldo():
    messagebox.showinfo("Saldo", f"{tili.name}: {tili.balance:.2f} €")

def talleta():
    tili.deposit(100.0)
    messagebox.showinfo("Talletus", "Talletettiin 100 € tilille.")

def nosta():
    if tili.balance >= 50.0:
        tili.withdrawal(50.0)
        messagebox.showinfo("Nosto", "Nostettiin 50 € tililtä.")
    else:
        messagebox.showerror("Virhe", "Ei tarpeeksi rahaa.")

tk.Button(root, text="Näytä saldo", command=näytä_saldo).pack(pady=10)
tk.Button(root, text="Talleta 100 €", command=talleta).pack(pady=10)
tk.Button(root, text="Nosta 50 €", command=nosta).pack(pady=10)
root.mainloop()