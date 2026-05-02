tablica = [1, 5, 7, 8, 3, 20, 7]
szukana = int(input("Jakiej liczby szukamy?"))

i = 0
N = len(tablica)
znaleziono = False

while i < N:
    if tablica[i] == szukana:
        znaleziono = True
        break
    i += 1

if znaleziono:
    print("Znaleziono liczbę")
else:
    print("Nie znaleziono")