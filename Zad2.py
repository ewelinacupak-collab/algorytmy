def count_paths(n, m):
    if n == 1 or m == 1:
        return 1

    return n * count_paths(n - 1, m - 1)

if __name__ == '__main__':
    print(count_paths(2, 3))
    print(count_paths(2, 0))