from tkinter import *
from tkinter import ttk, messagebox
from tuotteet import tuote, tuoteluettelo
from pankkitili import Account

class ComboBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x250")
        self.root.title("Valitse tuote")
        self.tili = Account("Käyttäjä", 100.0)

        self.catalog = tuoteluettelo()
        self._init_catalog()
        self._create_widgets()
        self.pankkisivu()


    def _init_catalog(self):
        # Esimerkkejä tuotteista
        self.catalog.lisaa_tuote(tuote("Apple", 1.50, "Fruit"))
        self.catalog.lisaa_tuote(tuote("Banana", 0.75, "Fruit"))
        self.catalog.lisaa_tuote(tuote("Carrot", 0.50, "Vegetable"))
        self.catalog.lisaa_tuote(tuote("Doughnut", 2.00, "Snack"))
        self.catalog.lisaa_tuote(tuote("Eggplant", 1.25, "Vegetable"))
        self.catalog.lisaa_tuote(tuote("Fig", 2.50, "Fruit"))
    
    def _create_widgets(self):
        # Lue UI-elementit
        valikko = Frame(self.root)
        valikko.pack(pady=10)

        self.combo = ttk.Combobox(valikko, values=self.catalog.hae_tuotteet())
        self.combo.set("Valitse tuote")
        self.combo.pack(pady=5)

        Label(valikko, text="Määrä:").pack(pady=5)
        self.maara = Entry(valikko, width=10)
        self.maara.insert(0, "1")
        self.maara.pack(pady=5)
        
        Button(self.root, text="Näytä valinta", command=self.show_selection).pack(pady=5)
        
        self.result_label = Label(self.root, text="")
        self.result_label.pack(pady=10)
    
    def show_selection(self):
        selected_item = self.combo.get()
        try:
            quantity = int(self.maara.get())
            self.result_label.config(text=f"Valittu tuote: {selected_item}, Määrä: {quantity}")
        except ValueError:
            messagebox.showerror("Virhe", "Anna kelvollinen määrä.")

    def pankkisivu(self):
        Label(self.root, text="Pankkitilin tilanne").pack(pady=10)
        Button(self.root, text="Näytä saldo", command=self.saldo).pack(pady=5)
        Button(self.root, text="Talleta 100 €", command=self.talleta).pack(pady=5)
        Button(self.root, text="Nosta 50 €", command=self.show_selection).pack(pady=5)

    def saldo(self):
        messagebox.showinfo("Saldo", f"{self.tili.name}: {self.tili.balance:.2f} €")

    def talleta(self):
        self.tili.deposit(100.0)
        messagebox.showinfo("Talletus", "Talletettiin 100 € tilille.")
