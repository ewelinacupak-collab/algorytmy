def knapsack(W, weights, values, n):
    # Tworzymy tabelę DP o wymiarach (n + 1) x (W + 1) zainicjalizowaną zerami
    # dp[i][w] będzie przechowywać maksymalną wartość dla i pierwszych przedmiotów i pojemności w
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Wypełniamy tabelę DP od dołu do góry (bottom-up)
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # Indeks aktualnego przedmiotu w listach weights i values to i - 1
            current_weight = weights[i - 1]
            current_value = values[i - 1]

            if current_weight <= w:
                # Mamy dwa wybory:
                # 1. Bierzemy przedmiot: dodajemy jego wartość i sprawdzamy najlepszy wynik dla reszty pojemności
                # 2. Nie bierzemy przedmiotu: zostaje wynik z poprzedniego wiersza dla tej samej pojemności
                dp[i][w] = max(current_value + dp[i - 1][w - current_weight], dp[i - 1][w])
            else:
                # Przedmiot jest za ciężki, nie zmieści się w plecaku o pojemności w
                dp[i][w] = dp[i - 1][w]

    # Maksymalna wartość znajduje się w prawym dolnym rogu tabeli
    max_value = dp[n][W]

    # --- Opcjonalnie: Odtwarzanie, które przedmioty zostały wybrane ---
    selected_items = []
    w = W
    for i in range(n, 0, -1):
        # Jeśli wartość się zmieniła w stosunku do poprzedniego wiersza, oznacza to, że przedmiot został wybrany
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # zapamiętujemy indeks przedmiotu (0-indexed)
            w -= weights[i - 1]  # zmniejszamy dostępną pojemność

    selected_items.reverse()  # Odwracamy listę, aby przedmioty były w kolejności rosnącej

    return max_value, selected_items


# --- Test działania programu ---
if __name__ == "__main__":
    # Dane wejściowe
    W = 50  # Maksymalna pojemność plecaka
    weights = [10, 20, 30]  # Wagi przedmiotów
    values = [60, 100, 120]  # Wartości przedmiotów
    n = len(weights)  # Liczba przedmiotów

    max_val, items = knapsack(W, weights, values, n)

    print(f"Maksymalna wartość w plecaku: {max_val}")
    print(f"Indeksy wybranych przedmiotów: {items}")
    print(f"Wagi wybranych przedmiotów: {[weights[i] for i in items]}")
    print(f"Wartości wybranych przedmiotów: {[values[i] for i in items]}")