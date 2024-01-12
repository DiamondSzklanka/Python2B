def metoda(p):
    b = p
    while abs(b-p/b) > 0.00001:
        b = (b+p/b)/2
    return b

print(metoda(int(input())))