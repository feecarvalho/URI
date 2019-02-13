while True:
    try:
        hora = [int(x) for x in input().split(':')]
        if hora[0] < 7:
            print('Atraso maximo: 0')
        else:
            atraso = (hora[0] - 7) * 60 + hora[1]
            print('Atraso maximo: {}'.format(atraso))
    except EOFError:
        break
