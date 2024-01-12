Liczby = []
p = 0
n = int(input())
for i in range(10,99):
    if i % 19 == 0:
        Liczby.append(i)
        p +=1
    if p == n:
        break
print(Liczby)