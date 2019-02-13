while True:
    N = int(input())
    mlen = N
    sm = 1
    aux = 1
    matriz = []

    if N == 0:
        print('', end='')
        break

    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(sm)
        matriz.append(linha)

    while N - 2 > 0:
        for i in range(aux, N - 1):
            for j in range(aux, N - 1):
                matriz[i][j] = sm + 1
        sm += 1
        aux += 1
        N -= 1

    for i in matriz:
        aux = 0
        for j in i:
            if aux == 0:
                print('{}'.format(str(j).rjust(3)), end='')
                aux += 1
            else:
                print('{}'.format(str(j).rjust(4)), end='')
            print(end='')
        aux += 1
        print('')
    print('\n', end='')
