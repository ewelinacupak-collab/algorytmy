import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

if a == 0:
    print("To nien jest równanie kwadratowe")
else:
    delta = b*b - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)

        print("Dwa pierwiastki", x1, x2)
    elif delta == 0:
        x0 = (-b)/(2*a)

        print("Jeden pierwiastek", x0)
    else:
        print("Brak pierwiastków")