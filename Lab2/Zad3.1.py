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

    def szukaj(self, x):
        """
        Fukncja wyszukuje na liście podaną wartość.
        Parametry: self - lista, x - szukana wastość
        Funkcja zwraca: True/False czy wartość jest w liście

        Wyjątki:
        - lista jest pusta (while inspektro is not none)
        - szukana wartość jest w pierwszym wagonie (inspektor = self.head)

        Złożoność:
        - czasowa: O(n)
        - pamięciowa: O(1)
        """

        inspektor = self.head

        while inspektor is not None:
            if inspektor.data == x:
                return True
            inspektor = inspektor.next

        return False

if __name__ == "__main__":

    moje_wagoniki = LinkedList()

    dane = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    for liczba in dane:
        moje_wagoniki.append(liczba)

    print(moje_wagoniki.szukaj(77))