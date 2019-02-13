fib = int(input())
var = 0
aux = -1
aux_2 = 1
cont = 0
fibo = []
while cont < fib:
    var = aux + aux_2
    aux = aux_2
    aux_2 = var
    fibo.append(var)
    cont += 1
print(*fibo, sep=' ')
