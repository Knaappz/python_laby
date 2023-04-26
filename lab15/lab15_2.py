class Shop:
    def __init__(self, nazwa, lok_sklepu):
        self.nazwa_sklepu = nazwa
        self.lok_sklepu = lok_sklepu

    def sprzedaj_piwo(self, piwo):
        print(f"Sprzedano piwo {piwo.nazwa} w sklepie {self.nazwa_sklepu} w mieście {self.lok_sklepu}")


class Beer(Shop):
    piwa = []

    def __init__(self, nazwa, rodzaj, cena, procenty, ocena):
        super().__init__("Monopol Kasia","Wrocław")
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.cena = cena
        self.procenty = procenty
        self.ocena = ocena
        Beer.piwa.append(self)

    def sprzedaj(self):
        super().sprzedaj_piwo(self)

    def po_ocenie(self):
        return sorted(self, key=lambda p: p.ocena, reverse=True)

    def po_nazwie(self):
        return sorted(self, key=lambda p: p.nazwa)

    @classmethod
    def dodaj_nowe_piwo(self):
        nazwa = input("Podaj nazwę piwa: ")
        rodzaj = input("Podaj rodzaj piwa: ")
        cena = float(input("Podaj cenę piwa: "))
        procenty = float(input("Podaj procenty alkoholu w piwie: "))
        ocena = int(input("Podaj ocenę piwa (0-10): "))
        pochodzenie = input("Podaj pochodzenie piwa: ")

        nowe_piwo = self(nazwa, rodzaj, cena, procenty, ocena, pochodzenie)
        return nowe_piwo


piwo1 = Beer("Perła Export", "pilzner", 5, 5.2, 5)
piwo2 = Beer("Żubr", "jasny lager", 5, 6.0, 10)
piwo3 = Beer("Lech", "jasne pełne", 6, 5.2, 2)
piwo4 = Beer("Somersby", "oranżada", 7, 4.5, 1)
piwo5 = Beer("Zetecky", "dolna fermentacja", 5, 5.0, 9)
piwo6 = Beer("Romper", "kto to wie", 3, 7.0, 0, )

lista_piw = [piwo1, piwo2, piwo3, piwo4, piwo5, piwo6]

# sort_piw = Beer.po_ocenie(lista_piw)
# sort_piw_po_nazwie = Beer.po_nazwie(lista_piw)

# for piwo in sort_piw:
#     print(piwo.nazwa, " - ocena: ", piwo.ocena,"/10")
#
# print("\nPosortowane piwa po nazwie:")
# for piwo in sort_piw_po_nazwie:
#     print(piwo.nazwa)

# nowe_piwo = Piwo.dodaj_nowe_piwo()
# print("\nDodano nowe piwo:")
# print("Nazwa: ", nowe_piwo.nazwa)
# print("Rodzaj: ", nowe_piwo.rodzaj)
# print("Cena: ", nowe_piwo.cena)
# print("Procenty: ", nowe_piwo.procenty)
# print("Ocena: ", nowe_piwo.ocena)
# print("Pochodzenie: ", nowe_piwo.pochodzenie)

piwo1.sprzedaj()
