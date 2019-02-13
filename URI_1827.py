from math import ceil

while True:
    try:
        matrixSize = int(input())
        matrix = []

        # Cria uma matriz com valores 0
        for i in range(matrixSize):
            line = []
            for j in range(matrixSize):
                line.append(0)
            matrix.append(line)

        for i in range(matrixSize):
            for j in range(matrixSize):
                if i == j:
                    matrix[i][j] = 2
                elif (i + j) == (matrixSize - 1):
                    matrix[i][j] = 3

        subMatrix = matrixSize / 3
        subMatrix = ceil(subMatrix)
        if subMatrix % 2 == 0:
            subMatrix += 1
        subMatrixStart = int((matrixSize - 1) / 2 - ((subMatrix - 1) / 2))  # Acha o indice inicial da subMatriz (1)
        subMatrixEnd = int((matrixSize - 1) / 2 + ((subMatrix - 1) / 2))  # Indice final

        for indI in range(subMatrixStart, subMatrixEnd + 1):
            for indJ in range(subMatrixStart, subMatrixEnd + 1):
                matrix[indI][indJ] = 1
                if (indI == (matrixSize - 1) / 2) and (indJ == (matrixSize - 1) / 2):
                    matrix[indI][indJ] = 4

        # Imprime a matriz
        for i in matrix:
            for j in i:
                print(j, end='')
            print()
        print()

    except(EOFError):
        break
