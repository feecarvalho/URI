N = int(input())

qtd = []

for n in range(0, N):
    qtd.append(int(input()))

for n in qtd:
    if n % 2 == 0 and n < 0:
        print('EVEN NEGATIVE')
    elif n % 2 == 0 and n > 0:
        print('EVEN POSITIVE')
    elif n == 0:
        print('NULL')
    elif n % 2 != 0 and n > 0:
        print('ODD POSITIVE')
    else:
        print('ODD NEGATIVE')
