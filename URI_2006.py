N = int(input())
esc = [int(x) for x in input().split(' ')]
aux = 0
for num in esc:
    if num == N:
        aux += 1
print(aux)
