x = input()
y = x[::-1]
def dzielniki(x,y):
    suma = int(x) + int(y)
    dzielniki = [i for i in range(1, suma + 1) if suma % i == 0]
    dzielniki.sort(reverse=True)
    return dzielniki[:2]

print(dzielniki(x,y))