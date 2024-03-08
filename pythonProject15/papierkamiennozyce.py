import random
nozyce = 1
papier = 2
kamien = 3
print("nozyce to 1, papier to 2, kamien to 3")
n = int(input("ilosc gier: "))
for i in range(n):
    a = random.randint(1,3)
    odp = int(input())
    if odp == a:
        print("remis")
    elif odp == 1  and a == 2:
        print("wygrales")
    elif odp == 2 and a == 3:
        print("wygrales")
    elif odp == 3 and a == 1:
        print("wygrales")
    elif odp == 1 and a == 3:
        print("przegrales")
    elif odp == 2 and a == 1:
        print("przegrales")
    elif odp == 3 and a == 2:
        print("przegrales")
    else:
        print("cO")
    print("Komputer wybral: " + str(a))


