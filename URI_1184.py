matriz = []
op = input()
aux = 0
total = 0
cont = 0
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)
for line in matriz:
    for value in range(0, aux):
        total += line[value]
        aux += 1
    cont += 1
    aux = cont
if op == 'S':
    print('%0.1f' % total)
elif op == 'M':
    print('%0.1f' % (total / 66))
