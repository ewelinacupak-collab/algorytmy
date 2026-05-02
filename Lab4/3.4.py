def sortuj_zagn(dane):
    for podlista in dane:
        podlista.sort()
    return dane

lista = [[5, 2, 9], [8, 1, 3], [7, 6, 4]]

posortowana_lista = sortuj_zagn(lista)
print(posortowana_lista)