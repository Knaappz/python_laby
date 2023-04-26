class Obywatel:
    def __init__(self, imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc

    @classmethod
    def twoje_dane(cls):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        ulica = input("Podaj ulice: ")

        while True:
            try:
                nr_domu = int(input("Podaj nr domu: "))
                break
            except ValueError:
                print("Błędne dane. Numer domu musi być liczbą.")

        kod_pocztowy = input("Podaj swój kod pocztowy: ")
        miejscowosc = input("Podaj miejscowosc: ")

        nowy_obywatel = cls(imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc)
        return nowy_obywatel

    def zapis(self, nazwa_pliku):
        with open(nazwa_pliku, "w") as f:
            wizytowka = f"------------- \n {self.imie} {self.nazwisko} \n {self.ulica} {self.nr_domu} \n {self.kod_pocztowy} {self.miejscowosc} \n--------------"
            f.write(wizytowka)
            print(wizytowka)

obywatel1 = Obywatel.twoje_dane()
obywatel1.zapis('dane1.txt')


