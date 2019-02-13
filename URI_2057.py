n = [int(i) for i in input().split(' ')]
hora = 0
for i in n:
    hora += i

if hora >= 24:
    hora -= 24
elif hora < 0:
    hora = 24 + hora
print(hora)
