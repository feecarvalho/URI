while True:
    N = int(input())
    aux = 0
    matriz = []
    ig = 1

    if N == 0:
        print('', end='')
        break

    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(1)
        matriz.append(linha)

    test = 1
    for i in range(0, N):
        for j in range(0, N):
            if aux >= 1:
                if i > j:
                    matriz[i][j] = ig
                    ig -= 1
                else:
                    matriz[i][j] = ig
                    ig += 1
            else:
                matriz[i][j] = ig
                ig += 1
        ig = test + 1
        test += 1
        aux += 1

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
