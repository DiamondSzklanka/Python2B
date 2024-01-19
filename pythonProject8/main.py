import math

f = open('temp.txt', 'r')
txt = f.read()
Temperatury = txt.split("\n")
a = 0
print(Temperatury)

for i in range(len(Temperatury)):
    b = int(Temperatury[i])
    if  b < 0:
        a += 1
print(a)
b = 100
for i in range(len(Temperatury)):
    if int(Temperatury[i]) < b:
        b = int(Temperatury[i])
print(b)
c = 0
for i in range(len(Temperatury)):
    c = c + int(Temperatury[i])
sr = c / len(Temperatury)
print(round(sr))
d = 0
for i in range(len(Temperatury)):
    if int(Temperatury[i]) >= 0:
        d +=1
print(d)
e = 0
LiczbyPierwsze = []
for i in range(len(Temperatury)):
    for j in range(2, int(Temperatury[i])):
        if (int(Temperatury[i]) % j) == 0:
            e +=1
            LiczbyPierwsze.append(int(Temperatury[i]))
            break
print(e)
print(LiczbyPierwsze)

f = 0
Kwadraty = []
for i in range(len(Temperatury)):
    if  math.sqrt(int(Temperatury[i])) == int:
        f += 1
        Kwadraty.append(Temperatury[i])
print(f)
print(Kwadraty)