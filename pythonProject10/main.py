import random
t = [[random.randint(1,100) for kol in range(10)] for wiersz in range(10)]
print(t)
for i in range(len(t)):
    if t[i][1] > t[i+1][1]:
        print("Trzymaj tak dalejjjjj")
    else:
        print("Bierz sie do orboty stary")