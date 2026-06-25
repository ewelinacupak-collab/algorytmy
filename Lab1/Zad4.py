tablica = [4, 20, 6, 8, 4, 2]
N = len(tablica)

min = tablica[0] #zakładamy, że first element is the lowest
i = 1 #start from second element

#przeszukujemy
while i < N:
    #jak element przeszukiwany is lower than nasz element minimalny
    if tablica[i] < min:
        min = tablica[i] #aktualizujemy go

    i += 1 #idziemy next

print(min)
