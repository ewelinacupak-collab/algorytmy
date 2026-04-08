class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def remove(self, i):
        """
        Funkcja usuwa i-ty węzeł listy, węzły ponumerowane od 1.
        Parametry: self - lista, i - węzeł do usunięcia
        Funkcja zwraca: listę z usniętnym wagonikiem

        Wyjątki: pusta lista

        Złożoność:
        - czasowa O(n)
        - pamięciowa O(1)
        """

        if self.head == None:
            return

        if i == 1:
            self.head = self.head.next
            return

        inspektor = self.head
        licznik = 1

        while licznik < i - 1:
            inspektor = inspektor.next
            licznik = licznik + 1

        if inspektor.next is not None:
            inspektor.next = inspektor.next.next
        else:
            print("Błąd, nie ma wagonika")

if __name__ == "__main__":

    moje_wagoniki = LinkedList()

    for liczba in [10, 30, 40, 50]:
        moje_wagoniki.append(liczba)

    print("Przed usunięciem miejsca 2", moje_wagoniki.display())

    moje_wagoniki.remove(2)

    print("Po usunięciu", moje_wagoniki.display())