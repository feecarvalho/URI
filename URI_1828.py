T = int(input())

for i in range(T):
    entrada = input().split(' ')
    sh, raj = entrada

    if sh == raj:
        print('Caso #{}: De novo!'.format(i + 1))
    elif sh == 'tesoura':
        if raj == 'papel' or raj == 'lagarto':
            print('Caso #{}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sh == 'papel':
        if raj == 'pedra' or raj == 'Spock':
            print('Caso #{}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sh == 'pedra':
        if raj == 'lagarto' or raj == 'tesoura':
            print('Caso #{}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sh == 'lagarto':
        if raj == 'Spock' or raj == 'papel':
            print('Caso #{}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sh == 'Spock':
        if raj == 'tesoura' or raj == 'pedra':
            print('Caso #{}: Bazinga!'.format(i + 1))
        else:
            print('Caso #{}: Raj trapaceou!'.format(i + 1))
