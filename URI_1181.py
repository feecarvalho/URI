matriz = []
line = int(input())
oper = input()
total = 0
for i in range(0, 12):
    linha = []
    for j in range(0, 12):
        x = float(input())
        linha.append(x)
    matriz.append(linha)

for num in matriz[line]:
    total += num

if oper == 'S':
    print(total)
elif oper == 'M':
    print('%0.1f' % (total / 12))
