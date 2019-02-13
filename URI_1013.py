valores = input().split(" ")
a, b, c = valores

maior = (int(a) + int(b) + abs(int(a) - int(b))) / 2
resultado = (maior + int(c) + abs(maior - int(c))) / 2

print('%d eh o maior' % resultado)
