def sumaLiczb():
    suma = 0

    for liczba in range(10, 100):
        for i in range(2, int(liczba**0.5) + 1):
            if liczba % i == 0:
                break
        else:
            suma += liczba

    return suma

print(sumaLiczb())
