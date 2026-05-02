def drugi_max(arr):
    """Funkcja przyjmuje tablicę liczb i zwraca drugi max element
    Parametry: arr- lista
    Funkcja zwraca: int/float drugi największy element

    Wyjątki:
    - gdy lista zawiera mniej niż dwa elementy
    - gdy wszystkie elementy są jednakowe (brak drugiego największego)

    Złożoność:
    - czasowa: O(n)
    - pamięciowa O(1)

    """

    if len(arr) < 2:
        raise ValueError("Tablica musi zawierać co najmniej 2 elementy")

    max1 = float("-inf")
    max2 = float("-inf")

    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x

    if max2 == float("-inf"):
        raise ValueError("Brak druguego największego elementu")

    return max2

if __name__ == "__main__":

    print(drugi_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(drugi_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(drugi_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(drugi_max([1]))