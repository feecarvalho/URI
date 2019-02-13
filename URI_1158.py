n = int(input())
aux = 0
while n > 0:
    numbers = input().split(' ')
    x, y = numbers
    x = int(x)
    y = int(y)
    while y > 0:
        if (x % 2) != 0:
            aux += x
            x += 1
            y -= 1
        else:
            x += 1
    n -= 1
    print(aux)
    aux = 0
