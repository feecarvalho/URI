caso_teste = int(input())

while caso_teste > 0:
    total = 0
    nome = input()
    nivel = float(input())
    menor = 11.0
    maior = -1.0
    notas = [float(x) for x in input().split(' ')]

    for i in range(0, 7):
        if (notas[i] > maior):
            maior = notas[i]
        if (notas[i] < menor):
            menor = notas[i]
        total += notas[i]
    total -= maior + menor
    print('{} {:.2f}'.format(nome, total * nivel))
    caso_teste -= 1
