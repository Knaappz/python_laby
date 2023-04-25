# zad3
def cm(a):
    x = 30.48 * a
    return str(x) + "cm"

def m(a):
    x = 0.3048 * a
    return str(x) + "m"

def km(a):
    x = 0.0003048 * a
    return str(x) + "km"

def mm(a):
    x = 304.8 * a
    return str(x) + "mm"

print(cm(int(input("Podaj wartośc w stopach: "))))
print(m(int(input("Podaj wartośc w stopach: "))))
print(km(int(input("Podaj wartośc w stopach: "))))
print(mm(int(input("Podaj wartośc w stopach: "))))

