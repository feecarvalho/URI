values = input().split(' ')
x, y = values
x = int(x)
y = int(y)
cont = 1

for num in range(1, y + 1):
    if (num % x) == 0:
        print(cont)
        cont += 1
    else:
        print(cont, end=' ')
        cont += 1
