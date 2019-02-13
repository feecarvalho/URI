caso = 1
while True:
    try:
        n = int(input())
        lista = [0]
        for i in range(n + 1):
            for num in range(i):
                lista.append(i)
        if n == 0:
            print('Caso {}: {} numero'.format(caso, len(lista)))
            print(*lista)
            print()
            caso += 1
        else:
            print('Caso {}: {} numeros'.format(caso, len(lista)))
            print(*lista, sep=' ')
            print()
            caso += 1
    except EOFError:
        break
