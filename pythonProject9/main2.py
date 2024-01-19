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
        if z[j] == 0:
            x +=1
        if z[j] == 1:
            y += 1
        else:
            print("wtf")

