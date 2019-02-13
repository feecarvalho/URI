casos = int(input())
while casos > 0:
    valores = input().split(' ')
    R1, R2 = valores
    print(int(R1) + int(R2))
    casos -= 1
