while True:
    T = int(input())
    matriz = []
    aux = 1

    if T == 0:
        break

    for i in range(T):
        linha = []
        for j in range(T):
            linha.append(aux)
        matriz.append(linha)

    for i in range(T):
        for j in range(T):
            matriz[i][j] = aux
            aux *= 2
        aux = matriz[i][0]
        aux *= 2

    count = len(str((matriz[i][j])))

    for i in matriz:  # Imprime a matriz
        for j in range(T):
            if j < T - 1:
                print('{:{}d}'.format(i[j], count), end=' ')
            else:
                print('{:{}d}'.format(i[j], count), end='')
        print()
    print()
