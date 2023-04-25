class Pojazd:
    def __init__(self, nazwa, nr_tablicy, szybkosc):
        self.nazwa = nazwa
        self.nr_tablicy = nr_tablicy
        self.szybkosc = szybkosc

    def jazda(self):
        print(f"Pojazd {self.nazwa} jedzie z prędkością {self.szybkosc} km/h.")

class Auto(Pojazd):
    def __init__(self, nr_tablicy,szybkosc):
        super().__init__('Audi',nr_tablicy, szybkosc)

    def drift(self):
        print(f'{self.nazwa} leci bokiem przez Auchan z prędkością {self.szybkosc} km/h.')

class Motor(Pojazd):
    def __init__(self,nr_tablicy, szybkosc):
        super().__init__('Yamaha',nr_tablicy,szybkosc)

    def wheelie(self):
        print(f'Jednostka policji nr12: Motor {self.nazwa} z nr {self.nr_tablicy} robi wheelie przez cały most! \n'
              f'Zgarnąć go!')

audi = Auto('DWL4874',50)
audi.drift()

yamaha = Motor('DWL6666', 60)
yamaha.wheelie()
