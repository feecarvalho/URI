while True:
    try:
        data = [int(x) for x in input().split(' ')]
        mes, dia = data
        calendario = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total = 0
        if mes == 12 and dia > 25:
            print('Ja passou!')
        elif mes == 12 and dia == 25:
            print('E natal!')
        elif mes == 12 and dia == 24:
            print('E vespera de natal!')
        else:
            for x in calendario[mes - 1:]:
                total += x
            total -= dia
            print('Faltam {} dias para o natal!'.format(total - 6))
    except EOFError:
        break
