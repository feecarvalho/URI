valores = [int(x) for x in input().split(" ")]

A, B, C, D = valores

if B > C and D > A and C + D > A + B and C > 0 and D > 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
