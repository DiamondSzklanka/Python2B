import random
def programZgaduje():
    najmn = 0
    najwk = 1001
    Zgadniecie = False
    while not Zgadniecie:
        x = random.randint(najmn + 1,najwk - 1)
        odp = input("Czy liczba o której myślisz to " + str(x) + "? ").lower()
        if odp in ["wieksza", "w"]:
            najmn = x
        elif odp in ["mniejsza", "m"]:
            najwk = x
        elif odp in ["tak", "zgadles", "dobrze"]:
            Zgadniecie = True
            return x
        else:
            print("Doprecyzuj")
print("Twoja liczba to: ", str(programZgaduje()))

