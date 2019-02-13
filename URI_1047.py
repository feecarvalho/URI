valores = [int(x) for x in input().split()]

x1, x2, t1, t2 = valores

inicio = (x1 * 60) + x2
fim = (t1 * 60) + t2
duracao = 0

if x1 <= t1:
    duracao = fim - inicio
    if duracao == 0:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracao / 60, duracao % 60))
else:
    duracao = (1440 - inicio) + fim
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracao / 60, duracao % 60))
