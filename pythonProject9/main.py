def blizniak(num):
    min = num-2
    max = num+2
    if num == 1 or min == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0 or (min % i-2) ==0 or (max % i+2) ==0:
                return False
    else:
        return True

print(blizniak(int(input())))