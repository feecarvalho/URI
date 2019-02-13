num = input().split()
A, B, C, D = num
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if A < B + C and B < A + C and C < A + B:
    print('S')
elif A < D + C and D < A + C and C < A + D:
    print('S')
elif A < B + D and B < A + D and D < A + B:
    print('S')
elif D < B + C and B < D + C and C < D + B:
    print('S')
else:
    print('N')
