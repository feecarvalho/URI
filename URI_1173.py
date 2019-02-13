values = []
x = int(input())
for num in range(0, 10):
    values.append(x)
    x *= 2
    print('N[%d] = %d' % (num, values[num]))
