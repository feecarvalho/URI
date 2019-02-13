import math

valores = input().split(" ")

A, B, C = valores

try:
    if A != 0:
        delta = (pow(float(B), 2)) - 4 * float(A) * float(C)
        x1 = (-float(B) + math.sqrt(delta)) / (2 * float(A))
        x2 = (-float(B) - math.sqrt(delta)) / (2 * float(A))
        print('R1 = %0.5f\nR2 = %0.5f' % (x1, x2))
except:
    print('Impossivel calcular')
