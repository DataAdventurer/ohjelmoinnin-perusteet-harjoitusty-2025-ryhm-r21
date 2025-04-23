#r21
#Maripuu Kristofer, Petter Paananen, Perälä Aapeli
class tuote:
    def __init__(self, nimi, hinta, tuoteryhmä):
        self.name = nimi
        self.price = hinta
        self.category = tuoteryhmä

    def __str__(self):
        return f"{self.name} ({self.price:.2f} €)"
    
class tuoteluettelo:
    def __init__(self):
        self.tuotteet = []

    def lisaa_tuote(self, tuote):
        self.tuotteet.append(tuote)

    def nayta_tuotteet(self):
        for tuote in self.tuotteet:
            print(tuote)
    
    def hae_tuotteet(self):
        return [str(tuote) for tuote in self.tuotteet]