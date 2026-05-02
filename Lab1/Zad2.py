N = int(input("Podaj ilość liczb, które chcesz sprawdzić"))
ile_ujemnych = 0
i = 0

while i < N:
    liczba = float(input("Podaj liczbę"))

    if liczba < 0:
        ile_ujemnych += 1

    i += 1
print(" Liczba ujemnych to", ile_ujemnych)