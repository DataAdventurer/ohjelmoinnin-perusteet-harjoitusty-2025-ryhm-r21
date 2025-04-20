from tkinter import *
from tkinter import ttk
from tuotteet import tuote, tuoteluettelo

class ComboBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x250")
        self.root.title("Valitse tuote")
        
        self.catalog = tuoteluettelo()
        self._init_catalog()
        self._create_widgets()
    
    def _init_catalog(self):
        # Esimerkkejä tuotteista
        self.catalog.lisaa_tuote(tuote("Apple", 1.50, "Fruit"))
        self.catalog.lisaa_tuote(tuote("Banana", 0.75, "Fruit"))
    
    def _create_widgets(self):
        # Lue UI-elementit
        self.combo = ttk.Combobox(self.root, values=self.catalog.hae_tuotteet())
        self.combo.set("Valitse tuote")
        self.combo.pack(pady=10)
        
        Button(self.root, text="Näytä valinta", command=self.show_selection).pack(pady=5)
        
        self.result_label = Label(self.root, text="")
        self.result_label.pack(pady=10)
    
    def show_selection(self):
        self.result_label.config(text=f"Selected: {self.combo.get()}")