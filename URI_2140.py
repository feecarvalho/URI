while True:
    notas = [100, 50, 20, 10, 5, 2]
    entrada = [int(x) for x in input().split(' ')]
    valor_total, valor_pago = entrada
    if valor_pago == 0 and valor_total == 0:
        break
    total = valor_pago - valor_total

    if total == 200:
        print('possible')
        continue
    count = 0
    for nota in notas:
        if total >= nota:
            total -= nota
            count += 1
            for nota in notas:
                if total >= nota:
                    total -= nota
                    count += 1
    if total == 0 and count == 2:
        print('possible')
    else:
        print('impossible')
