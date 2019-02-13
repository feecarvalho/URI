n = int(input())
aux = 0
while n > 0:
    value = int(input())
    for num in range(1, value + 1):
        if ((value % num) == 0):
            aux += num
    if aux == value + 1:
        print(value, 'eh primo')
    else:
        print(value, 'nao eh primo')
    aux = 0
    n -= 1
