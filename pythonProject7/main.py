import random
def nieparzysta(Tab):
    for i in range(len(Tab)):
        if Tab[i] % 2 != 0:
            return True
            break
def zlozona(Tab):
    for i in range(len(Tab)):
        for j in range (Tab[i]):
            if Tab[i] % (j+1) == 0:
                if j != i and j != 1:
                    return True
                break
Tab = []
for i in range(2):
    Tab.append((random.randint(0, 50)))
print(Tab)
print(nieparzysta(Tab))
print(zlozona(Tab))
print(Tab[::-1])