N = int(input())

for num in range(1, (N + 1)):
    if (num % 2) == 0:
        print('%d^2 = %d' % (num, (num ** 2)))
