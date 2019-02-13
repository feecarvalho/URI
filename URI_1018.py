valor = int(input())

print(valor)

if valor >= 100:
    notas = valor / 100
    print('%0.0d nota(s) de R$ 100,00' % notas)
    valor = valor % 100
else:
    print('0 nota(s) de R$ 100,00')
if valor >= 50:
    notas = valor / 50
    print('%0.0d nota(s) de R$ 50,00' % notas)
    valor = valor % 50
else:
    print('0 nota(s) de R$ 50,00')
if valor >= 20:
    notas = valor / 20
    print('%0.0d nota(s) de R$ 20,00' % notas)
    valor = valor % 20
else:
    print('0 nota(s) de R$ 20,00')
if valor >= 10:
    notas = valor / 10
    print('%0.0d nota(s) de R$ 10,00' % notas)
    valor = valor % 10
else:
    print('0 nota(s) de R$ 10,00')
if valor >= 5:
    notas = valor / 5
    print('%0.0d nota(s) de R$ 5,00' % notas)
    valor = valor % 5
else:
    print('0 nota(s) de R$ 5,00')
if valor >= 2:
    notas = valor / 2
    print('%0.0d nota(s) de R$ 2,00' % notas)
    valor = valor % 2
else:
    print('0 nota(s) de R$ 2,00')
if valor >= 1:
    notas = valor / 1
    print('%0.0d nota(s) de R$ 1,00' % notas)
else:
    print('0 nota(s) de R$ 1,00')
