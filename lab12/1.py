# zad1
import math
def obliczenia():
    a = int(input("Podaj wartość 'a': "))
    b = int(input("Podaj wartość 'b': "))

    x = a - b
    y = a + b
    z = a * b
    u = a / b
    s = math.sqrt(a)
    ss = math.sqrt(b)

    print("Odejmowanie: ", x)
    print("Dodawanie: ", y)
    print("Mnożenie: ", z)
    print("Dzielenie: ", u)
    print("Pierwiastek z" + str(a) + ":", s)
    print("Pierwiastek z" + str(b) + ":", ss)

obliczenia()
