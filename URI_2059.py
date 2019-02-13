n = [int(x) for x in input().split(' ')]
p, j1, j2, r, a = n
jogador1_mensagem = 'Jogador 1 ganha!'
jogador2_mensagem = 'Jogador 2 ganha!'

if p == 1:
    if (j1 + j2) % 2 == 0:
        if r == 1 == a:
            print(jogador2_mensagem)
        else:
            print(jogador1_mensagem)
    else:
        if r == 1 and a != 1:
            print(jogador1_mensagem)
        else:
            print(jogador2_mensagem)
elif p == 0:
    if (j1 + j2) % 2 != 0:
        if r == 1 == a:
            print(jogador2_mensagem)
        else:
            print(jogador1_mensagem)
    else:
        if r == 1 and a != 1:
            print(jogador1_mensagem)
        else:
            print(jogador2_mensagem)
