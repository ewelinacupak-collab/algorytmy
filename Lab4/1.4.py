def sortuj_liste():
    input_str = input("Podaj liczby oddzielone spacją: ")

    try:
        lista = [int(item) for item in input_str.split()]
    except ValueError:
        print("Niepoprawne liczby")
        return

    typ = input("Wybierz typ sortowania: A - rosnąco, B - malejąco")

    if typ == "A":
        lista.sort()
        print("Posortowana lista rosnąco ", lista)
    elif typ == "B":
        lista.sort(reverse=True)
        print("Posortowana lista malejąco ", lista)
    else:
        print("Niepoprawny typ sortowania")

if __name__ == "__main__":
    sortuj_liste()