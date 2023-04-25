class Animals:
    def __init__(self, gatunek, rasa, imie, typ, region_wys, predkosc):
        self.gatunek = gatunek
        self.rasa = rasa
        self.imie = imie
        self.typ = typ
        self.region_wys = region_wys
        self.predkosc = predkosc

    def wystepowanie(self):
        return f'Gatunek {self.gatunek}, {self.rasa}, region występowania: {self.region_wys} '


class Cat(Animals):
    def __init__(self, region_wys):
        super().__init__("Kot", "Munchkin", "Gacek", "miesożerca", region_wys, 48)

    def drapansko(self):
        return f'{self.gatunek} {self.rasa} ostrzy pazurki na drapaku.'


class Dog(Animals):
    def __init__(self, region_wys, predkosc):
        super().__init__("Pies", "Border Collie", "Borys", "wszystkożerca", region_wys, predkosc)

    def poscig(self, pr_lisa):
        if self.predkosc >= 50:
            print(f'{self.imie} jest w trakcie poscigu...')
            if pr_lisa > self.predkosc:
                print(f'Nie udało się dogonić lisa.')
            elif pr_lisa < self.predkosc:
                print(f'Udało się złapać lisa!')
        elif self.predkosc < 50:
            print(f'{self.imie} jest za wolny na ten pościg')


class Bird(Animals):
    def __init__(self, imie, region_wys):
        super().__init__("Ptak", "Struś", imie, "roślinożerca", region_wys, 70)

    def ustaw_imie(self):
        return f'Urodził się nowy struś o imieniu {self.imie}!'


class Fish(Animals):
    def __init__(self, region_wys):
        super().__init__("Ryba", "Rekin Biały", "Dango", "miesożerca", region_wys, 40)


kot1 = Cat("Cały Świat")
print(kot1.wystepowanie())
print(kot1.drapansko())

# borys = Dog("Europa", 50)
# borys.poscig(51)

# strus = Bird("Stasiu", "Afryka")
# print(strus.ustaw_imie())

# ptak1 = Bird("Afryka")
# print(ptak1.wystepowanie())
#
# ryba1 = Fish("Ocean Spokojny")
# print(ryba1.wystepowanie())
