while True:
    try:
        string = input()
        p1, p2 = 0, 0
        lista = []
        fecha = False

        for i in string:
            if i == '(':
                p1 += 1
                lista.append(i)
            elif i == ')':
                p2 += 1
                lista.append(i)
                if (p1 - p2) < 0:
                    p2 = -100

        if len(lista) % 2 != 0:
            fecha = True
        else:
            if lista[0] == ')':
                fecha = True
            else:
                if lista[len(lista) - 1] == '(':
                    fecha = True
                else:
                    if p2 < -10:
                        fecha = True
                    else:
                        fecha = False

        if fecha:
            print('incorrect')
        else:
            print('correct')
    except EOFError:
        break
