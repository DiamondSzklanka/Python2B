boki = []
for i in range(3):
    boki.append((int(input())))
boki.sort()
def trojkat(x,y,z):
    if x + y > z:
        return True
    else:
        return False

print(trojkat(boki[0],boki[1],boki[2]))
