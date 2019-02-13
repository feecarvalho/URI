val = [float(x) for x in input().split(' ')]
N1, N2 = val
print('{:.2f}%'.format(((N2 / N1) - 1) * 100))
