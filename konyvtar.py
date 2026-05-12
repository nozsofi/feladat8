class Konyv:
    def __init__(self, cim, szerzo):
        self.cim = cim
        self.szerzo = szerzo

    def __str__(self):
        return f"{self.cim} - {self.szerzo}"

class Konyvtar:

    def __init__(self):
        self.konyvek = []

    def hozzad(self, konyv):
        self.konyvek.append(konyv)

    def __str__(self):
        return "\n".join(str(konyv) for konyv in self.konyvek)

    def listaz(self):
        print(self)

konyvtar = Konyvtar()
konyvtar.hozzad(Konyv("A Gyűrűk Ura", "J.R.R. Tolkien"))
konyvtar.hozzad(Konyv("Harry Potter és a bölcsek köve", "J.K. Rowling"))
konyvtar.hozzad(Konyv("A szél árnyéka", "Carlos Ruiz Zafón"))

konyvtar.listaz()