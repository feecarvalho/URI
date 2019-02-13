from collections import Counter


def solucao(n1, n2):
    total = Counter([n1[i: i + len(n2)] for i in range(len(n1))])
    return total[n2]


count = 1
while True:
    try:
        n2 = input()
        n1 = input()
        print('Caso #{}:'.format(count))
        if n1.find(n2) == -1:
            print('Nao existe subsequencia')
            print()
        else:
            print('Qtd.Subsequencias: {}'.format(solucao(n1, n2)))
            print('Pos: {}'.format(n1.rfind(n2) + 1))
            print()
        count += 1
    except EOFError:
        break
