import random
a=random.randint(1,1000)
b=False
while b==False:
    odp=int(input())
    if odp>a:
        print("mniejsza")
    if odp<a:
        print("wieksza")
    if odp==a:
        print("Zgadles")
        break