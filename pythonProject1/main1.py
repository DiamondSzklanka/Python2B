def funkcja(x):

    if x == 1:
        return 1
    else:
        return (x * funkcja(x - 1))

print(funkcja(int(input())))
