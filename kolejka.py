#Dana jest lista liczb
#wstawiamy je do kolejnki
#zdejmujemy je i wyisujemy parzyste
from collections import deque

if __name__ == "__main__":
    liczby = [3, 8, 5, 3, 5, 9, 10]

    kolejka = deque()

    for x in liczby:
        kolejka.append(x)

    while kolejka:
        element = kolejka.popleft()

        if element % 2 == 0:
            print(element)

