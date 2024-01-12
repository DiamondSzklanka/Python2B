n = int(input())
Lista = []
p = 0
for i in range(999, 100, -1):
    if i % 37 == 0:
        Lista.append(i)
        p +=1
    if p == n:
        break
print(Lista)
