def oblicz_onp(wyrazenie):

    stos = []
    elementy = wyrazenie.split()

    for element in elementy:
        if element == '=':
            break
        elif element in '+-*/^':
            b = stos.pop()
            a = stos.pop()

            if element == '+': stos.append(a + b)
            elif element == '-': stos.append(a - b)
            elif element == '*': stos.append(a * b)
            elif element == '/': stos.append(a / b)
            elif element == '^': stos.append(a ** b)
        else:
            stos.append(float(element))

    return stos.pop()

wyrazenie = "3 44 + 5 * ="
wynik = oblicz_onp(wyrazenie)
print(wynik)


