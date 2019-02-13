x = int(input())
y = int(input())

aux = 0
if x < y:
    for num in range(x, y + 1):
        if (num % 13) != 0:
            aux += num
    print(aux)
if y < x:
    for num in range(y, x + 1):
        if (num % 13) != 0:
            aux += num
    print(aux)
