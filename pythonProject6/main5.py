n = 0

for i in range(100, 1000):
    x = i % 10         # liczba jednosci
    y = (i // 10) % 10 # liczba dziesiatek
    z = i // 100       # liczba setek


    if z > (x+y):
        n += 1

print(n)
