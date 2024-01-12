x = input()
y = x [::-1]
def funkcja(x,y):
    suma = int(x) + int(y)
    liczba = int(x[-1]) + int(y[-1])
    return suma % liczba == 0

print(funkcja(x,y))
