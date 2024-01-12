Znaki = []
Wyraz = ''
Odwrotnie = []
Upper = []
f = open('owoce.txt', 'r')  # f to str do ktorej importuje plik txt
txt = f.read()              # txt to str w ktorym odczytujemy zawartosc pliku txt
Owoce = txt.split("\n")     # Owoce to lista w ktorej sie wszystko pomiesci juz tak frfr
for i in range(len(Owoce)):
    Znaki.append(len(Owoce[i]))
for i in range(len(Owoce)):
    x = Owoce[i]
    Wyraz = Wyraz + x[0]
for i in range(len(Owoce)):
    x = Owoce[i]
    Odwrotnie.append(x[::-1])
max_dl = 0
owocek = ''
for i in range(len(Owoce)):
    if max_dl < Znaki[i]:
        max_dl = Znaki[i]
        owocek = Owoce[i]
for i in range(len(Owoce)):
    Upper.append(Owoce[i].upper())
print(Owoce)
print(Znaki)
print(Wyraz)
print(Odwrotnie)
print(max_dl)
print(owocek)
print(Upper)
