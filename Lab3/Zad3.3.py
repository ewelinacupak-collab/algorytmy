from collections import deque
import time

def symulacja(lista_uczestnikow, liczba_operacji):

    kolejka = deque(lista_uczestnikow)

    print("Start gry: ", lista_uczestnikow)
    print("Eliminacja następuje co", liczba_operacji, "kolejki")

    while len(kolejka) > 1:
        for i in range(liczba_operacji):
            uczestnik = kolejka.popleft()
            kolejka.append(uczestnik)

        eleiminowany = kolejka.popleft()
        print("Wyeliminowany/a został: ", eleiminowany)
        print("\n", kolejka)

    zwyciezca = kolejka.popleft()
    print("Zwycięzcą zostaje: ", zwyciezca)

    return zwyciezca 

lista_uczestnikow = ["Adam", "Ola", "Kasia", "Julia"]
liczba_operacji = 3

result = symulacja(lista_uczestnikow, liczba_operacji)
print(result)
