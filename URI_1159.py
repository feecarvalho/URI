x = int(input())
aux = 0
while x != 0:
    for num in range(x, x + 10):
        if (num % 2) == 0:
            aux += num
    print(aux)
    aux = 0
    x = int(input())
