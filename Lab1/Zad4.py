tablica = [4, 20, 6, 8, 4, 2]
N = len(tablica)

min = tablica[0]
i = 1

while i < N:
    if tablica[i] < min:
        min = tablica[i]

    i += 1

print(min)