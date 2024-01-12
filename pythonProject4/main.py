import math

def kwadraty (j):
    for i in range(int(j**2 /2)):
        suma = j**2
        c = suma /2
        a = i
        b = c-a
        if math.sqrt(a) % 1 == 0 and math.sqrt(b) % 1 == 0 and math.sqrt(c) % 1 == 0 and a+b+c == suma :
            return math.sqrt(a),math.sqrt(b),math.sqrt(c)

print(kwadraty((int(input()))))
