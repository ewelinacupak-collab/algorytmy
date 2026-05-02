def nawiasy(ciag):
    stos = []

    for znak in ciag:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if len(stos) == 0:
                return False
            else:
                stos.pop()


    return len(stos) == 0

if __name__ == "__main__":
    ciag = input("Podaj ciąg nawiasów:")

    if nawiasy(ciag):
        print("Nawiasy są poprawne")
    else:
        print("Nawiasy nie poprawne")
