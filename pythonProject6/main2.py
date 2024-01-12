suma = []
for i in range(100, 999):
    if i % 8 ==0 and i % 16 != 0:
        suma.append(i)
print(sum(suma))