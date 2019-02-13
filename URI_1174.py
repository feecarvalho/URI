values = []
for num in range(0, 100):
    x = float(input())
    if x <= 10:
        values.append(x)
        print('A[%d] = %0.1f' % (num, values[num]))
    else:
        values.append(x)
