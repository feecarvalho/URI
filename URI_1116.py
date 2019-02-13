n = int(input())

for i in range(0, n):
    values = input().split(' ')
    x, y = values
    x = int(x)
    y = int(y)

    if y == 0:
        print('divisao impossivel')
    else:
        print(x / y)
