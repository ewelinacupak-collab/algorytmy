#Zaimplementuj algorytm przesuwający elementy tablicy w lewo lub w prawo o zadany krok k.

def rotate_array(arr,k):
    """ Przesuwa listę 'arr' o 'k' pozycji.
    k > 0: w prawo
    k < 0: w lewo
    """

    n = len(arr)
    if n == 0:
        return arr

    #Normalizacja k

    k = k % n

    #[ostatnie k elementów] + [wszystkie lelemnty oprócz ostatnich]
    #W PRAWO

    return arr[-k:] + arr[:-k]

my_list = [1,2,3,4,5,6,7,8,9]

print(rotate_array(my_list, 15))

print(rotate_array(my_list, -1))
