valores = input().split(" ")
A, B, C = valores

triangulo = (float(A) * float(C)) / 2
circulo = 3.14159 * (float(C) * float(C))
trapezio = ((float(A) + float(B)) * float(C)) / 2
quadrado = float(B) * float(B)
retangulo = float(A) * float(B)

print('TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f' % (
triangulo, circulo, trapezio, quadrado, retangulo))
