class Auta():
    def __init__(self, marka, model, przebieg, moc_silnika, kolor, cena_auta, rodzaj):
        self.marka = marka
        self.model = model
        self.przebieg = przebieg
        self.moc_silnika = moc_silnika
        self.kolor = kolor
        self.cena_auta = cena_auta
        self.rodzaj = rodzaj

    def dragrace(self, predkosc):
        if predkosc > 90:
            wynik = self.moc_silnika
            return "Wygrałeś!"
        elif predkosc < 90:
            wynik = self.moc_silnika + 999
            return "Przegrałeś, silnik ci wybuchł", wynik

    def myjnia(self, cena):
        if cena > 100:
            k = self.kolor
            return "Wow jak nowe, nie wiedziałem że miałeś auto koloru "+ k
        elif cena < 100:
            b = "brudny"
            name = self.marka+' '+self.model
            return "Nie starczyło na całe mycie samochodu "+name+" jest "+ b

    def noweauto(self, taknie):
        if taknie == "tak":
            ma = input("Podaj marke: ")
            mo = input("Podaj model "+ma+' ')
            prz = input("Jaki przebieg minimalny: ")
            moc = input("Minimalna moc: ")
            kol = input("Jaki kolor lubisz: ")
            cena = input("Cena: ")
            ro = input("Rodzaj auta: ")
            nc = Auta(ma, mo, prz, moc, kol, cena, ro)
            return "Twoje nowe autko to: ", nc.marka, nc.model, nc.przebieg, nc.moc_silnika, nc.kolor, nc.cena_auta, nc.rodzaj
        else:
            return "Biedak..."


seat = Auta("Seat", "Ibiza", 200000, 105, "limonkowy", 14000, "heatchback")
opel_astra = Auta("Opel", "Astra", 25000, 95, "czerwony", 54000, "combi")
ferrari = Auta("Ferrari", "Portofino", 123000, 600, "czerwony", 60000, "cabriolet")

print(seat.dragrace(22))
print(opel_astra.myjnia(30))
print(seat.noweauto("tak"))


