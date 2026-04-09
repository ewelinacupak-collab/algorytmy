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

    def merge(self, lista1, lista2):
        """
        Funkcja scalająca dwie uporządkowane listy, w jedną uporządkowaną listę.
        Parametry: self1, self2 - dwie listy
        Funkcja zwraca: jedną listę, powstałą z tych dwóch, uporządkowaną

        Wyjątki:
        - jeden pociąg jest pusty (while p1 and p2, nie występuje)
        - oba pociągi są puste (pętla w ogóle nie ruszy)
        - pociągi mają różną długość (if p1: ogon.next = p1)

        Złożoność:
        -czasowa O(n)
        -pamięciowa O(1)
        """

        dummy = Node(0)
        ogon = dummy

        p1 = lista1.head
        p2 = lista2.head

        while p1 is not None and p2 is not None:
            if p1.data <= p2.data:
                ogon.next = p1
                p1 = p1.next
            else:
                ogon.next = p2
                p2 = p2.next
            ogon = ogon.next

        if p1 is not None:
            ogon.next = p1
        else:
            ogon.next = p2

        nowy_pociag = LinkedList()
        nowy_pociag.head = dummy.next
        return nowy_pociag

if __name__ == "__main__":

    a = LinkedList()
    for x in [1, 3, 5, 7]:
        a.append(x)

    b = LinkedList()
    for x in [2, 4, 6, 8]:
        b.append(x)

    wynik = a.merge(b)
    wynik.display()
