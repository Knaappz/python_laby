#zad1
def sprawdz_kod(kod):
    if not kod[:2].isdigit():
        raise ValueError("Ciąg liczb jest niepoprawny")
    elif kod[2] != '-':
        raise ValueError("Ciąg liczb jest niepoprawny")
    elif not kod[3:].isdigit():
        raise ValueError("Ciąg liczb jest niepoprawny")

with open("kody_pocztowe.txt", "a") as file:
    while True:
        kod = input("Podaj kod pocztowy (wpisz 'done' aby zakończyć): ")
        if kod == "done":
            print("Do zobaczenia :)")
            break

        try:
            sprawdz_kod(kod)
            print("Podany kod jest poprawny")

            file.write(kod + "\n")
            print("Kod pocztowy został zapisany do pliku 'kody_pocztowe.txt'")
        except ValueError as e:
            print("Błąd:", str(e))

#zad2