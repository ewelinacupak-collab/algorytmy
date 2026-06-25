#info ile liczb sprawdzić
N = int(input("Podaj ilość liczb, które chcesz sprawdzić"))
ile_ujemnych = 0 #pom, będziemy tu sumować
i = 0 # zmienna sterująca pętlą, licznik obrotów

#pętla wykona się N razy
while i < N:
    #w każdym obrocie prosimy o liczbę
    liczba = float(input("Podaj liczbę"))

    #check czy liczba większa od zera
    if liczba < 0:
        #tak, zwiększamy licznik
        ile_ujemnych += 1

    i += 1 #zwiąkszamy i, żeby nie była nieskończona
#po zakończeniu wypisujemy
print(" Liczba ujemnych to", ile_ujemnych)
