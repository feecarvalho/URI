N = int(input())
aux = 0
for i in range(0, N):
    ent = input().split(' ')
    x, y = ent
    x = int(x)
    y = int(y)
    if x < y:
        for num in range(x + 1, y):
            if num % 2 != 0:
                aux += num
        print(aux)
        aux = 0
    elif y < x:
        for num in range(y + 1, x):
            if num % 2 != 0:
                aux += num
        print(aux)
        aux = 0
    elif x == y or y == x:
        print(0)
