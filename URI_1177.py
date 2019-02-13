vetor = []
value = int(input())
x = 0
for num in range(0, 1000):
    for aux in range(0, value):
        vetor.append(aux)
while x < 1000:
    print('N[%d] = %d' % (x, vetor[x]))
    x += 1
