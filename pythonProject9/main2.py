Tab = []
Bin = []
for i in range(5):
    Tab.append(int(input()))
def Binarnie(n):
    return bin(n).replace("0b", "")
for i in range(5):
    Bin.append(Binarnie(Tab[i]))
print(Bin)
zera = []
jedynki = []
x = 0
y = 0
for i in range(5):
    z = Bin[i]
    for j in range(len(z)):
        if z[j] == 0 or '0':
            x +=1
        elif z[j] == 1 or '1':
            y += 1
    if x > y:
        print("ZERO")
    elif y > x:
        print("JEDEN")
    elif y == x:
        print("ROWNO")