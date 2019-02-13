N = int(input())

teste = []
coelhos = 0
sapos = 0
ratos = 0

for n in range(0, N):
    teste = input().split(' ')
    if teste[1] == 'C':
        coelhos += int(teste[0])
    elif teste[1] == 'S':
        sapos += int(teste[0])
    else:
        ratos += int(teste[0])

total = sapos + ratos + coelhos
print('Total:', total, 'cobaias')

print('Total de coelhos:', coelhos)
print('Total de ratos:', ratos)
print('Total de sapos:', sapos)

print('Percentual de coelhos: %0.2f' % (float(coelhos / total) * 100), '%')
print('Percentual de ratos: %0.2f' % (float(ratos / total) * 100), '%')
print('Percentual de sapos: %0.2f' % (float(sapos / total) * 100), '%')
