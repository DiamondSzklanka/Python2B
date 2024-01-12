n = 0

for i in range(10, 100):
    x = i % 10
    y = i // 10

    if y >= 2 * x:
        n += 1

print(n)
