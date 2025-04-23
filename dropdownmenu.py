#r21
#Maripuu Kristofer, Petter Paananen, Perälä Aapeli
from tkinter import *
from tkinter import ttk, messagebox
from tuotteet import tuote, tuoteluettelo
from pankkitili import Account

class ComboBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x250")
        self.root.title("Kauppasovellus")
        self.tili = Account("Käyttäjä", 100.0)
        self.korin_tuotteet = []
        self.korin_hinta = 0.0

        self.catalog = tuoteluettelo()
        self._init_catalog()
        self._create_widgets()
        self.pankkisivu()


    def _init_catalog(self):
        # Esimerkkejä tuotteista
        self.catalog.lisaa_tuote(tuote("Omena", 1.50, "Fruit"))
        self.catalog.lisaa_tuote(tuote("Banaani", 0.75, "Fruit"))
        self.catalog.lisaa_tuote(tuote("Porkkana", 0.50, "Vegetable"))
        self.catalog.lisaa_tuote(tuote("Donitsi", 2.00, "Snack"))
        self.catalog.lisaa_tuote(tuote("Munakoiso", 1.25, "Vegetable"))
        self.catalog.lisaa_tuote(tuote("Viikuna", 2.50, "Fruit"))
    
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
        
        button_frame = Frame(self.root)
        button_frame.pack(pady=10)
        Button(button_frame, text="Valitse", command=self.show_selection).pack(pady=5)
        Button(button_frame, text="Lisää ostoskoriin", command=self.add_to_cart).pack(pady=5)
        
        self.result_label = Label(self.root, text="")
        self.result_label.pack(pady=10)

        cart_frame = LabelFrame(self.root, text="Ostoskori")
        cart_frame.pack(pady=10, padx=10, fill=X)

        self.cart_listbox = Listbox(cart_frame, width=40, height=5)
        self.cart_listbox.pack(pady=5, padx=5, fill=X)

        self.total_label = Label(cart_frame, text=f"Yhteensä: {self.korin_hinta:.2f} €")
        self.total_label.pack(side=RIGHT, padx=5, pady=5)
        
        # Lisää tyhjennysnappi
        Button(cart_frame, text="Tyhjennä ostoskori", command=self.clear_cart).pack(side=LEFT, padx=5, pady=5)
        # ostamisnappi
        Button(cart_frame, text="Osta", command=self.purchase).pack(side=LEFT, padx=5, pady=5)
    
    def show_selection(self):
        selected_item = self.combo.get()
        try:
            quantity = int(self.maara.get())

            tuote_hinta = 0
            for item in self.catalog.tuotteet:
                if str(item) == selected_item:
                    tuote_hinta = item.price
                    break
            total_price = quantity * tuote_hinta

            
            
            
            self.result_label.config(text=f"Valittu tuote: {selected_item}, Määrä: {quantity}, Hinta: {tuote_hinta:.2f} €, Yhteensä: {total_price:.2f} €")
        except ValueError:
            messagebox.showerror("Virhe", "Anna kelvollinen määrä.")

    def add_to_cart(self):
        selected_item = self.combo.get()
        try:
            quantity = int(self.maara.get())

            current_product = None
            for item in self.catalog.tuotteet:
                if str(item) == selected_item:
                    current_product = item
                    break
            if current_product:

                item_price = current_product.price * quantity


                cart_item = f"{selected_item} x {quantity} - {item_price:.2f} €"
                self.korin_tuotteet.append((current_product, quantity, item_price))
                self.cart_listbox.insert(END, cart_item)

                self.korin_hinta += item_price
                self.total_label.config(text=f"Yhteensä: {self.korin_hinta:.2f} €")

                messagebox.showinfo("Ostoskorin lisäys", f"{selected_item} lisätty ostoskoriin.")
            else:
                messagebox.showerror("Virhe", "Valitse tuote ensin.")
        except ValueError:
            messagebox.showerror("Virhe", "Anna kelvollinen määrä.")

    def clear_cart(self):
        self.korin_tuotteet.clear()
        self.cart_listbox.delete(0, END)
        self.korin_hinta = 0.0
        self.total_label.config(text=f"Yhteensä: {self.korin_hinta:.2f} €")
        messagebox.showinfo("Ostoskori tyhjennetty", "Ostoskori on tyhjennetty.")
    
    def purchase(self):
        if not self.korin_tuotteet:
            messagebox.showwarning("Ostoskori on tyhjä", "Ostoskorissa ei ole tuotteita.")
            return
        if self.tili.balance < self.korin_hinta:
            messagebox.showerror("Virhe", "Tilillä ei ole tarpeeksi varoja.")
            return
        total_hinta = self.korin_hinta
        self.tili.withdrawal(total_hinta)  # Vähennä hinta tililtä
        

        self.kuitin_luonti()  # Luo kuitti ostoksesta
        self.korin_tuotteet.clear()
        messagebox.showinfo("Osto onnistui", f"Ostettiin tuotteet yhteensä {self.korin_hinta:.2f} €.\nTilillä jäljellä: {self.tili.balance:.2f} €")
        self.clear_cart()  # Tyhjennä ostoskori ostoksen jälkeen
        
    def kuitin_luonti(self):
        from datetime import datetime
        

        

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"kuitit/kuitti_{timestamp}.txt"

        # kuitin sisältö
        
        kuitti_teksti = "============Kuitti============\n"
        kuitti_teksti += f"Ostaja: {self.tili.name}\n"
        kuitti_teksti += f"Päivämäärä: {now.strftime('%d.%m.%Y %H:%M:%S')}\n"
        kuitti_teksti += "==============================\n"
        kuitti_teksti += "Ostetut tuotteet:\n"

        for item, quantity, price in self.korin_tuotteet:
            kuitti_teksti += f"{item.name} x {quantity} - {price:.2f} €\n"
        kuitti_teksti += f"\nYhteensä: {self.korin_hinta:.2f} €\n"
        kuitti_teksti += f"Maksaja: {self.tili.name}\n"
        kuitti_teksti += f"Tilin saldo: {self.tili.balance:.2f} €\n"
        kuitti_teksti += "\nKiitos ostoksista!\n"
        kuitti_teksti += "==============================\n"

        try:
            with open(filename, "w") as file:
                file.write(kuitti_teksti)
            
        except Exception as e:
            messagebox.showerror("Virhe", f"Kuittia ei voitu luoda: {e}")

    def pankkisivu(self):
        Label(self.root, text="Pankkitilin tilanne").pack(pady=10)
        Button(self.root, text="Näytä saldo", command=self.saldo).pack(pady=5)
        Button(self.root, text="Talleta 100 €", command=self.talleta).pack(pady=5)
    

    def saldo(self):
        messagebox.showinfo("Saldo", f"{self.tili.name}: {self.tili.balance:.2f} €")

    def talleta(self):
        self.tili.deposit(100.0)
        messagebox.showinfo("Talletus", "Talletettiin 100 € tilille.")