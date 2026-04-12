stos = []

stos.append(10)
stos.append(20)
stos.append(30)

print("Stos", stos)

print("szczyt stosu", stos[-1])

print("element usunięty", stos.pop())

print("stos", stos)

if not stos:
    print("Pusty")
else:
    print("Stos nie jest pusty")