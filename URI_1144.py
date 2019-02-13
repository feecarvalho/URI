n = int(input())
lines = 0
aux = 1

while lines < n:
    print(aux, aux * aux, (aux * aux) * aux)
    print(aux, (aux * aux) + 1, ((aux * aux) * aux) + 1)
    lines += 1
    aux += 1
