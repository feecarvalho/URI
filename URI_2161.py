def fracao(vezes):
    fracao = 1 / 6
    if vezes != 0:
        for num in range(vezes - 1):
            fracao = 1 / (6 + fracao)
    else:
        fracao = 0
    return fracao + 3


n = int(input())

print('{:.10f}'.format(fracao(n)))
