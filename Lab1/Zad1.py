import math 

#wczytanie współczynników i na zmiennoprzecinkowe
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    #jak a 0 to jest to równanie liniowe przerywamy nie robimy
    print("To nien jest równanie kwadratowe")
else:
    #liczymy deltę
    delta = b*b - 4*a*c

    if delta > 0:
        #delta dodatnia dwa różna pierwiastki
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)

        print("Dwa pierwiastki", x1, x2)
    elif delta == 0:
        #delta zero jeden pierwiastek
        x0 = (-b)/(2*a)

        print("Jeden pierwiastek", x0)
    else:
        #delta ujemna
        print("Brak pierwiastków")
