N = int(input())

for i in range(N):
    T = int(input())
    if T < 2015:
        print('{} D.C.'.format(2015 - T))
    else:
        print('{} A.C.'.format(abs((T + 1) - 2015)))
