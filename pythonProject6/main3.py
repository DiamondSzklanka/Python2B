#najwieksza liczba dwucyfrowa podzielna przez 7
x = 0
for i in range(10,99):
    if i % 7 == 0:
        x = i
#liczba liczb czterocyfrowych podzielna przez ta liczbe
j = 0
for i in range(1000, 9999):
    if i % x == 0:
        j +=1
print(j)