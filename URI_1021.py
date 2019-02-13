N = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05]

if N >= 0 and N <= 1000000.00:
    print("NOTAS:")
    for nota in notas:
        qtd = N / nota
        print("%d nota(s) de R$ %0.2f" % (qtd, nota))
        N = N % nota

    print("MOEDAS:")
    for moeda in moedas:
        qtd = N / moeda
        print("%d moeda(s) de R$ %0.2f" % (qtd, moeda))
        N = N % moeda

    if (N / 0.01) > 0.9:
        qtd = N / 0.01
        print("%0.0f moeda(s) de R$ 0.01" % float(qtd))
    else:
        print("0 moeda(s) de R$ 0.01")
else:
    False
