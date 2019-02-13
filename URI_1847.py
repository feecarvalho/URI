temp = input().split(' ')
A, B, C = temp
A = int(A)
B = int(B)
C = int(C)

if B < A and C >= B:
    print(':)')
elif B > A and C <= B:
    print(':(')
elif B > A and (B - A) > (C - B):
    print(':(')
elif B > A and (B - A) <= (C - B):
    print(':)')
elif B < A and (A - B) > (B - C):
    print(':)')
elif B < A and (A - B) <= (B - C):
    print(':(')
elif B == A and C > B:
    print(':)')
else:
    print(':(')
