n = int(input())

for i in range(n):
    esc1 = input()
    esc2 = input()
    if esc1 == 'ataque':
        if esc2 == 'ataque':
            print('Aniquilacao mutua')
        else:
            print('Jogador 1 venceu')
    if esc1 == 'papel':
        if esc2 == 'papel':
            print('Ambos venceram')
        else:
            print('Jogador 2 venceu')
    if esc1 == 'pedra':
        if esc2 == 'pedra':
            print('Sem ganhador')
        elif esc2 == 'papel':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')
