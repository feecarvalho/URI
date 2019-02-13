n = int(input())
lista = [int(x) for x in input().split(' ')]
d2, d3, d4, d5 = 0, 0, 0, 0

for num in lista:
    if num % 2 == 0:
        d2 += 1
    if num % 3 == 0:
        d3 += 1
    if num % 4 == 0:
        d4 += 1
    if num % 5 == 0:
        d5 += 1
print('{} Multiplo(s) de 2'.format(d2))
print('{} Multiplo(s) de 3'.format(d3))
print('{} Multiplo(s) de 4'.format(d4))
print('{} Multiplo(s) de 5'.format(d5))
