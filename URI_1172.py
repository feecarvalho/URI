values = []
for num in range(0, 10):
    x = int(input())
    if x <= 0:
        x = 1
        values.append(x)
    else:
        values.append(x)
    print('X[%d] = %d' % (num, values[num]))
