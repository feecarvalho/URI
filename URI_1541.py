import math

values = input().split(' ')
a = values[0]
b = values[1]
c = values[2]

while a != 0:
    valor = ((int(a) * int(b)) * 100) / int(c)
    print('%0.0f' % int(math.sqrt(valor)))
    values = input().split(' ')
    if values[0] == '0':
        break
    else:
        a, b, c = values
