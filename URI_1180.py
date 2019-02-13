n = int(input())

x = list(map(int, input().split()))

aux = 1001
pos = 0

for num in range(0, n):
    if x[num] < aux:
        aux = x[num]
        pos = num

print('Menor valor: %d' % aux)
print('Posicao: %d' % pos)
