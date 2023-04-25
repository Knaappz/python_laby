class Piwo:
    def __init__(self, nazwa, rodzaj, cena, procenty, ocena, pochodzenie):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.cena = cena
        self.procenty = procenty
        self.ocena = ocena
        self.pochodzenie = pochodzenie

    def posortuj_po_ocenie(self):
        return sorted(self, key=lambda p: p.ocena, reverse=True)


piwo1 = Piwo("Perła Export", "pilzner", 5, 5.2, 5, "Lublin")
piwo2 = Piwo("Żubr", "jasny lager", 5, 6.0, 10, "Puszcza Białowieska")
piwo3 = Piwo("Lech", "jasne pełne", 6, 5.2, 2, "Wielkopolska")
piwo4 = Piwo("Somersby", "oranżada", 7, 4.5, 1, "Dania")
piwo5 = Piwo("Zetecky", "dolna fermentacja", 5, 5.0, 9, "Czechy")

lista_piw = [piwo1, piwo2, piwo3, piwo4, piwo5]
posortowane_piw = Piwo.posortuj_po_ocenie(lista_piw)
for piwo in posortowane_piw:
    print(piwo.nazwa, " - ocena: ", piwo.ocena,"/10")
