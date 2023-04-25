# zad4
c = int(input("Na jakiej wysokości lecimy (w metrach) ... "))
def lot(a):
    b = int(a)*0.001
    if int(b)<5:
        return str(b) + "km to za nisko"
    else:
        return str(b) + "km jesteś bezpieczny"
print(lot(c))

