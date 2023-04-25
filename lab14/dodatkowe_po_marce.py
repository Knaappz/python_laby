class Smartfon:
    listainst = []

    def __init__(self, marka, model, pamiec, procesor, kolor):
        self.marka = marka
        self.model = model
        self.pamiec = pamiec
        self.procesor = procesor
        self.kolor = kolor

        self.lista = [self.marka, self.model, self.pamiec, self.procesor, self.kolor]
        self.listainst.append(self)

    def modele_po_marce(self, marka):
        modele = [ins.model for ins in self.listainst
                  if ins.marka == marka]
        if modele:
            print(f"Modele {marka}:")
            for model in modele:
                print(f"- {model}")
        else:
            print(f"Brak modeli dla marki {marka}")

smart = Smartfon("Huiawei", "Modelowany", 100, "Duzy", "Czarny")
smart1 = Smartfon("Huiawei", "chujowy", 100, "Duzy", "Czarny")
smart2 = Smartfon("Huiawei", "chora", 100, "Duzy", "Czarny")
smart4 = Smartfon("Huiawei", "chnds", 100, "Duzy", "Czarny")
smart6 = Smartfon("Oppo", "Supertel1", 100, "Duzy", "Czarny")

smart.modele_po_marce("Oppo")


