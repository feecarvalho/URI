entry = int(input())
var = 0
aux = -1
aux_2 = 1
cont = 0
fibo = []
for num in range(0, 61):
    var = aux + aux_2
    aux = aux_2
    aux_2 = var
    fibo.append(var)

while entry > 0:
    cont = int(input())
    print('Fib(%d) = %d' % (cont, fibo[cont]))
    entry -= 1
