def funkcja(a, b, c):
    # arytmetyczny
    if b - a == c - b:
        arytmetyczny = "TAK"
    else:
        arytmetyczny = "NIE"

    # geometryczny
    if b / a == c / b:
        geometryczny = "TAK"
    else:
        geometryczny = "NIE"

    # rosnący
    if a < b < c:
        rosnacy = "TAK"
    else:
        rosnacy = "NIE"

    #ciąg malejący
    if a > b > c:
        malejacy = "TAK"
    else:
        malejacy = "NIE"

    return f"arytmetyczny-{arytmetyczny}; geometryczny-{geometryczny}; rosnacy-{rosnacy}; malejacy-{malejacy}"

Lista = []
for i in range(3):
    Lista.append(int(input()))
print(funkcja(Lista[0], Lista[1], Lista[2]))
