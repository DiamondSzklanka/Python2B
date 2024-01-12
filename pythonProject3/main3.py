def funkcja():
    for x in range(10):
        rozwiazania = []
        liczba = 304 + x * 10
        if liczba % 6 == 0 and liczba % 9 != 0:
            rozwiazania.append(x)
        return rozwiazania

print(funkcja())
