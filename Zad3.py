def count_ways(coins, amount):
    # Słownik memo: kluczem będzie krotka (indeks_monety, pozostała_kwota)
    memo = {}

    def recursive_change(index, current_amount):
        # Przypadek bazowy 1: Kwota została idealnie rozmieniona
        if current_amount == 0:
            return 1

        # Przypadek bazowy 2: Kwota stała się ujemna lub skończyły nam się monety
        if current_amount < 0 or index >= len(coins):
            return 0

        # Sprawdzenie, czy ten stan był już wcześniej obliczony
        state = (index, current_amount)
        if state in memo:
            return memo[state]

        # Rekurencja:
        # 1. Bierzemy aktualną monetę (zmniejszamy kwotę, indeks zostaje ten sam)
        # 2. Pomijamy aktualną monetę (kwota bez zmian, przechodzimy do kolejnego indeksu)
        use_coin = recursive_change(index, current_amount - coins[index])
        skip_coin = recursive_change(index + 1, current_amount)

        # Zapisujemy wynik w memoizacji i zwracamy go
        memo[state] = use_coin + skip_coin
        return memo[state]

    # Uruchamiamy rekurencję od pierwszego indeksu (0) i pełnej kwoty
    return recursive_change(0, amount)


# --- Test działania ---
coins = [1, 2, 5]
amount = 5
wynik = count_ways(coins, amount)

print(f"Liczba sposobów dla coins={coins} i amount={amount}: {wynik}")