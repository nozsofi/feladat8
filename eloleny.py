class Eloleny:
    def __init__(self, nev, eletkor):
        self.nev = nev
        self.eletkor = eletkor

class Noveny(Eloleny):
    def __init__(self, nev, eletkor, vizigeny):
        super().__init__(nev, eletkor)
        self.vizigeny = vizigeny

    def __str__(self):
        return f"Növény neve: {self.nev}, életkora: {self.eletkor} év, vizigeny: {self.vizigeny}"

class Allat(Eloleny):
    def __init__(self, nev, eletkor, labak_szama):
        super().__init__(nev, eletkor)
        self.labak_szama = labak_szama


    def __str__(self):
        return f"Allat neve: {self.nev}, életkora: {self.eletkor} év, labak_szama: {self.labak_szama}"

class Gomba(Eloleny):
    def __init__(self, nev, eletkor, mergezo_e):
        super().__init__(nev, eletkor)
        self.mergezo_e = mergezo_e

    def __str__(self):
        return f"Gomba neve: {self.nev}, életkora: {self.eletkor} év, mergezo_e: {self.mergezo_e}"

rozsa = Noveny("Rózsa", 3, 0.5)
macska = Allat("Macska", 7, 4)
csiperke = Gomba("Csiperke", 1, False)

print(rozsa)
print(macska)
print(csiperke)
