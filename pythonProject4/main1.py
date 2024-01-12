def trojkaty(n):
    lista_bokow_trojkatow = []

    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if c <= 0:
                break

            if a**2 + b**2 == c**2:
                trojkat = (a, b, c)
                lista_bokow_trojkatow.append(trojkat)

    return lista_bokow_trojkatow

# Przykład użycia:
print(trojkaty(int(input())))
