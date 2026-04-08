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
        while temp.next:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def wstaw_posortowane(self, nowa_wartosc):

        """
            Funkcja zapisuje do listy liczby, tak, by w każdym momencie była posortowana.
            Parametry: lista - lista, x - element do dodania
            Funkcja zwraca: posortowaną listę z nowym atrgumentem.

            Wyjątki:
            - lista jest pusta, lub nowa wartość jest mniejsza od głowy
            Złożoność:
            - czasowa O(n)
            - pamięciowa O(1)
            """
        nowy_wagon = Node(nowa_wartosc)

        if self.head == None or self.head.data >= nowa_wartosc:
            nowy_wagon.next = self.head
            self.head = nowy_wagon
            return

        szukacz = self.head
        while szukacz.next is not None and szukacz.next.data < nowa_wartosc:
            szukacz = szukacz.next

        nowy_wagon.next = szukacz.next
        szukacz.next = nowy_wagon

if __name__ == "__main__":

    pociag = LinkedList()

    for x in [10, 20, 30, 40, 50]:
        pociag.append(x)

    print("Pociąg przed wstawieniem:")
    pociag.display()

    pociag.wstaw_posortowane(25)

    print("Pociąg po wstawieniu:")
    pociag.display()