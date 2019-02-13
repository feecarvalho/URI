vetor = []
pos = 19
for n in range(0, 20):
    vetor.append(int(input()))

for num in range(0, 10):
    aux = vetor[num]
    vetor[num] = vetor[pos]
    vetor[pos] = aux
    pos -= 1

for num in range(0, 20):
    print('N[%d] = %d' % (num, vetor[num]))
