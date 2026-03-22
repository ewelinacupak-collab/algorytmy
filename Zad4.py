#Napisz funkcję usuwającą i-ty węzeł z listy (węzły numerujemy od 1).

def usun_i_ty_element(lista, i):
    """
    Usuwa i-ty element z listy (indeksy od 1).
    """

    if 1 <= i <= len(lista):
        del lista[i-1]
    else:
        return lista

moja_lista =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(moja_lista)

usun_i_ty_element(moja_lista, 1)
print(moja_lista)