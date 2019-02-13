n = int(input())
aux = 0
while n > 0:
    value = int(input())
    for num in range(1, value):
        if (value % num == 0):
            aux += num
    if aux == value:
        print(value, 'eh perfeito')
    else:
        print(value, 'nao eh perfeito')
    aux = 0
    n -= 1
