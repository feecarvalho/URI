n = int(input())
lines = 0
aux = 1

while lines < n:
    print(aux, aux * aux, (aux * aux) * aux)
    lines += 1
    aux += 1
