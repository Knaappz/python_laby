slowo = input("Wprowadź słowo: ")
literki = list(slowo)
literki.reverse()

wypisane_literki = ' '.join(literki)
odw_slowo = "".join(literki)

print("Odwrócone słowa:", odw_slowo)
if odw_slowo == slowo:
    print("To słowo jest palindromem.")
else:
    print("To słowo nie jest palindromem.")


