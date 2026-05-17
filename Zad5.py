def min_coins(coins, amount):
    # Tworzymy tablicę dp o rozmiarze (amount + 1)
    # Inicjalizujemy ją wartością nieskończoności (float('inf')),
    # ponieważ szukamy minimum.
    dp = [float('inf')] * (amount + 1)

    # Przypadek bazowy: aby uzyskać kwotę 0, potrzebujemy 0 monet
    dp[0] = 0

    # Obliczamy minimalną liczbę monet dla każdej kwoty od 1 do amount
    for i in range(1, amount + 1):
        for coin in coins:
            # Jeśli moneta nie jest większa niż aktualna kwota 'i'
            if coin <= i:
                # Sprawdzamy, czy użycie tej monety da nam mniejszą liczbę monet
                # niż to, co do tej pory znaleźliśmy dla kwoty 'i'
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Jeśli dp[amount] nadal wynosi nieskończoność, oznacza to,
    # że tej kwoty nie da się rozmienić podanymi monetami
    return dp[amount] if dp[amount] != float('inf') else -1


# --- Test działania programu ---
coins = [1, 3, 4]
amount = 6

wynik = min_coins(coins, amount)
print(f"Minimalna liczba monet dla kwoty {amount} to: {wynik}")