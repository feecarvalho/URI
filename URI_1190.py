matriz = []
op = input()
total = 0
cont = 11
temp = 12
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)
for i in range(1, 6):
    for j in range(cont, temp):
        total += matriz[i][j]
    cont -= 1
cont = 7
for i in range(6, 11):
    for j in range(cont, temp):
        total += matriz[i][j]
    cont += 1
if op == 'S':
    print('%0.1f' % total)
elif op == 'M':
    print('%0.1f' % (total / 30))
