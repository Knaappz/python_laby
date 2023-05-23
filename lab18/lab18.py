#z1

# with open("pantadeusz.txt") as plik:
#     for linia in plik:
#         print (linia.strip().split())


# with open("pantadeusz.txt") as plik:
#     for linia in plik:
#         print (linia)

#z2 (bez enumerate)

# import linecache
# wiersze = [8, 12, 60, 98, 104]
# plik = 'pantadeusz.txt'

# for numer_w in wiersze:
#     wiersz = linecache.getline(plik, numer_w)
#     print(wiersz)

#z2 (z enumerate)

# import linecache
# wiersze = [8, 12, 60, 98, 104]
# plik = 'pantadeusz.txt'

# with open(plik, 'r') as file:
#     for index, numer_w in enumerate(wiersze, start=1):
#         wiersz = linecache.getline(plik, numer_w)
#         print(f"Line {index}: {wiersz}")

#z3

# stos1 = []
# stos2 = []
# stos3 = []

# foo1 = open('stosik1.txt', 'w')
# for i in range(50):
#     stos1.append(i)
#     i+=1
#     foo1.writelines(str(i)+' ')

# foo2 = open('stosik2.txt', 'w')
# for i in range(100):
#     stos2.append(i)
#     i+=1
#     foo2.writelines(str(i)+' ')

# foo3 = open('stosik3.txt', 'w')
# for i in range(150):
#     stos3.append(i)
#     i+=1
#     foo3.writelines(str(i)+' ')

#z4





