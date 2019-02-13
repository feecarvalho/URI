x = float(input())
n = []
n.append(x)

print('N[0] = %0.4f' % x)
for num in range(1, 100):
    x = x / 2
    n.append(x)
    print('N[%d] = %0.4f' % (num, n[num]))
