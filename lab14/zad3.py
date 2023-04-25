import math

class Figura:
    def obwod(self):
        pass

    def pole(self):
        pass


class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def obwod(self):
        return 4 * self.bok

    def pole(self):
        return self.bok ** 2


class Prostokat(Figura):
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b

    def obwod(self):
        return 2 * self.bok_a + 2 * self.bok_b

    def pole(self):
        return self.bok_a * self.bok_b


class Trojkat(Figura):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def obwod(self):
        return 3 * self.podstawa

    def pole(self):
        return 0.5 * self.podstawa * self.wysokosc


class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien

    def pole(self):
        return math.pi * self.promien ** 2


class Romb(Figura):
    def __init__(self, przekatna_a, przekatna_b):
        self.przekatna_a = przekatna_a
        self.przekatna_b = przekatna_b

    def obwod(self):
        return 4 * math.sqrt(0.25 * self.przekatna_a ** 2 + 0.25 * self.przekatna_b ** 2)

    def pole(self):
        return 0.5 * self.przekatna_a * self.przekatna_b


class Trapez(Figura):
    def __init__(self, podstawa_a, podstawa_b, wysokosc):
        self.podstawa_a = podstawa_a
        self.podstawa_b = podstawa_b
        self.wysokosc = wysokosc

    def obwod(self):
        return self.podstawa_a + self.podstawa_b + 2 * math.sqrt(
            (0.5 * (self.podstawa_a - self.podstawa_b)) ** 2 + self.wysokosc ** 2)

    def pole(self):
        return 0.5 * (self.podstawa_a + self.podstawa_b) * self.wysokosc


# Przykład użycia:

print("Obliczanie pola i obwodu figur")
print("1. Kwadrat")
bok_kwadratu = float(input("Podaj długość boku kwadratu: "))
kwadrat = Kwadrat(bok_kwadratu)
print("Pole kwadratu:", kwadrat.pole())
print("Obwód kwadratu:", kwadrat.obwod())
