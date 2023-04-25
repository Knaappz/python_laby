#1

import  random
class Restaurant:
    def __init__(self, nazwa, rodzaj, ocena, lokalizacja):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.ocena = ocena
        self.lokalizacja = lokalizacja

    def o_nas(self):
        print(f'{self.nazwa} to {self.rodzaj} z oceną {self.ocena} w miescie {self.lokalizacja}.')


class Stoisko(Restaurant):
    def __init__(self, nazwa, rodzaj, ocena, lokalizacja):
        super().__init__(nazwa, rodzaj, ocena, lokalizacja)
        self.smaki = ['czekolada', 'wanilia', 'truskawka', 'malina']

    def smaki_lodow(self):
        print(f"Smaki w {self.nazwa} to:")
        for smaki in self.smaki:
            print(f"- {smaki}")


class CoffeShop(Restaurant):
    def __init__(self, nazwa, rodzaj, ocena, lokalizacja):
        super().__init__(nazwa, rodzaj, ocena, lokalizacja)
        self.kawy = {'espresso': 9.0, 'cappuccino': 13.0, 'latte': 15.0, 'americano': 8.0, 'flat white': 13.5}

    def menu(self):
        print(f"Menu w {self.nazwa}:")
        for kawa, cena in self.kawy.items():
            print(f"- {kawa}: {cena} PLN")

    def menu_1niedostepna(self):
        print(f"Menu w {self.nazwa}:")
        niedostepna = random.choice(list(self.kawy.keys()))
        for kawa, cena in self.kawy.items():
            if kawa == niedostepna:
                print(f'- {kawa} jest aktualnie niedostępna')
            else:
                print(f"- {kawa}: {cena} PLN")

    def tanie(self):
        naj = min(self.kawy, key=self.kawy.get)
        cena = self.kawy[naj]
        print(f"Najtańsza kawa w {self.nazwa} to: {naj}, cena: {cena} PLN")

    def nowa_kawa(self, nazwa, cena):
            self.kawy[nazwa] = cena
            print(f"Nowa kawa '{nazwa}' została dodana do menu.")


# budka = Restaurant('Lody na kółkach', 'lodziarnia', '5/5 gwiazdek', 'Brzeg Dolny')
# budka.o_nas()
#
# budka = Stoisko('Lody na kółkach', 'lodziarnia', '5/5 gwiazdek', 'Brzeg Dolny')
# budka.smaki_lodow()
#
# coffie = CoffeShop('Lodówka','kawiarnia','4/5 giazdek','Wołów')
# coffie.menu()
# print(' ')
# coffie = CoffeShop('Lodówka','kawiarnia','4/5 giazdek','Wołów')
# coffie.menu_1niedostepna()
# coffie = Restaurant('Lodówka','kawiarnia','4/5 giazdek','Wołów')
# coffie.o_nas()
# coffie = CoffeShop('Lodówka','kawiarnia','4/5 giazdek','Wołów')
# coffie.tanie()
# coffie.nowa_kawa("double espresso", 10.0)
# coffie.menu()