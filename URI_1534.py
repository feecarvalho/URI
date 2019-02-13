while True:
    try:
        N = int(input())
        matriz = []

        for i in range(N):  # Cria e popula a matriz com 0
            linha = []
            for j in range(N):
                linha.append(0)
            matriz.append(linha)

        for i in range(0, N):  # Organiza os numeros dentro da matriz
            for j in range(0, N):
                if i == j and (
                        i + j) != N - 1:  # Se os indices forem iguais add 1 exceto quando estiver no centro da matriz
                    matriz[i][j] = 1
                elif (i + j) == N - 1:  # Se a soma dos indices for igual a N add 2
                    matriz[i][j] = 2
                else:
                    matriz[i][j] = 3  # Se nao add 3

        for i in matriz:  # Imprime a matriz
            for j in i:
                print(j, end='')
            print()

    except(EOFError):
        break
