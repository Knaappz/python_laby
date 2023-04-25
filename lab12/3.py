# zad2
import math

def kula(r):
    pole = math.pi * r ** 2
    objetosc = 4 / 3 * r ** 3

    return pole, objetosc


print(kula(int(input("Podaj r: "))))

def stozek(r, l, h):
    pole_p = math.pi * r ** 2
    pole_b = math.pi * r * l

    pole_c = pole_b + pole_p

    objetosc = 1 / 3 * pole_p * h
    return pole_c, objetosc


print(stozek(2 ,4, 5))

def szescian(a):
    pole_c = 6*a**2
    objetosc = a**3

    return pole_c, objetosc

print(szescian(int(input("Podaj a: "))))
