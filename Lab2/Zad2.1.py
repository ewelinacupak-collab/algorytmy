def rotate_array(arr,k):
    """ Przesuwa listę 'arr' o 'k' pozycji.
    k > 0: w prawo
    k < 0: w lewo
    """
    n = len(arr)
    if n == 0:
        return arr

    nowa_tablica = [0] * n

    for i in range(n):
        nowa_position = (i + k) % n
        nowa_tablica[nowa_position] = arr[i]

    return nowa_tablica

if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    print(rotate_array(my_list, 5))