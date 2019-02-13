N = int(input())

testes = []

for num in range(0, N):
    testes.append(int(input()))

auxO = 0
auxI = 0

for num in testes:
    if num >= 10 and num <= 20:
        auxI += 1
    else:
        auxO += 1

print(auxI, 'in')
print(auxO, 'out')
