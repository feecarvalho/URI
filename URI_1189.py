matriz = []
op = input()
total = 0
cont = 0
temp = 1
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)
for i in range(1, 6):
    for j in range(cont, temp):
        total += matriz[i][j]
    temp += 1
temp = 5
for i in range(6, 11):
    for j in range(cont, temp):
        total += matriz[i][j]
    temp -= 1
if op == 'S':
    print('%0.1f' % total)
elif op == 'M':
    print('%0.1f' % (total / 30))
