import random
x=random.randint(1,1000)
bool=False
while not bool:
    odp=int(input("Zgaduj typie: "))
    if odp>x:
        print("mniejsza")
    if odp<x:
        print("wieksza")
    if odp==x:
        print("Zgadles")
        bool = True