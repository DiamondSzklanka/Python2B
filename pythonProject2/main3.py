def trojkaty(n):
    boki = []
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                boki.append((a, b, c))
    return boki

n = int(input())
print(trojkaty(n))
