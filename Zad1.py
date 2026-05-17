def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

if __name__ == '__main__':
    print(power(2, 3))
    print(power(2, 0))
    print(power(2, 5))