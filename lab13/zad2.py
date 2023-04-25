import random

class Book:
    def __init__(self, tytul, autor, rok_wydania, liczba_stron, cena):
        self.tytul= tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.liczba_stron = liczba_stron
        self.cena = cena

    def czytaj(self):
        return f"Metoda 1: Czytanie książki {self.tytul} autorstwa {self.autor}..."

    def promocja(self, obnizka):
        nowa_cena = self.cena - obnizka
        return f"Metoda 2: Książka {self.tytul} została przeceniona z {self.cena}zl " \
               f"na {nowa_cena}zl"

    def zmiana_autora(self, nowy_autor):
        self.autor = nowy_autor
        return f"Metoda 3: Wprowadzono pomyłkę. Kiążkę {self.tytul} napisał {self.autor}."

    def wyswietl_tytuly(self):
        for book in self:
            print(book.tytul)

    def reklama(self):
        return f"Już są!!! Nowe wydanie {self.tytul} w Empik!!!"

    def srednia_cena(self):
        suma_cen = sum(book.cena for book in self)
        sr_cena = suma_cen / len(self)
        return sr_cena


book1 = Book("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997, 223, 35)
book2 = Book("W pustyni i w puszczy", "Henryk Sienkiewicz", 1910, 318, 25)
book3 = Book("Marsjanin", "Andy Weir", 2011, 385, 40)
book4 = Book("Władca Pierścieni: Drużyna Pierścienia", "J.R.R. Tolkien", 1954, 423, 68)
book5 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, 215, 25)

books = [book1, book2, book3, book4, book5]

srednia_cena = Book.srednia_cena(books)
print(f"Średnia cena książek: {srednia_cena}")
print(book1.czytaj())
print(book5.promocja(20))
print(book3.zmiana_autora("Krzysztof Krafczyk"))
Book.wyswietl_tytuly(books)
print(book1.reklama())
