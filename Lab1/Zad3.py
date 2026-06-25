tablica = [1, 5, 7, 8, 3, 20, 7]
szukana = int(input("Jakiej liczby szukamy?"))

i = 0 #zaczynamy od pierwszego elementu
N = len(tablica) #długość tablicy
znaleziono = False #domyślnie zakłądamy, że liczby brak

#przechodzimy przez all tablicę
while i < N:
    if tablica[i] == szukana:
        znaleziono = True #jak element pod indexem jest równy szukanej zmieniamy wartość
        break #przerywamy
    i += 1 #do kolejnego indexu

#sprawdzamy stan i piszemy
if znaleziono:
    print("Znaleziono liczbę")
else:
    print("Nie znaleziono")
