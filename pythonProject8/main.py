f = open('temp.txt', 'r')
txt = f.read()
Temperatury = txt.split("\n")
a = 0
print(Temperatury)
print(Temperatury[7])
for i in range(len(Temperatury)):
    b = int(Temperatury[i])
    if  b < 0:
        a += 1
print(a)