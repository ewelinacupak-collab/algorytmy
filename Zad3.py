#Napisz funkcję wyszukującą na liście podaną wartość.

def znajdz_wartosc(lista,cel):
    """
    Fukncja przeszukuje listę w poszukiwaniu wartości.
    Zwraca indeks elementu, jeślio zostanie znaleziony.
    W przeciwnym razie zwraca -1.
    """

    for i in range(len(lista)):
        if lista[i] == cel:
            return i
    return -1

moja_lista =[1, 2, 3, 4, 5, 6, 7, 8, 9]
szukana = 9

wynik = znajdz_wartosc(moja_lista,szukana)

if wynik != -1:
    print("Szukana wartość ma indeks", wynik)
else:
    print("Szukana wartość nie występuje w zbiorze")