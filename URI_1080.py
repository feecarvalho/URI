aux = 0
posi = 0

for n in range(0, 100):
    value = int(input())
    if value > aux:
        aux = value
        posi = n + 1

print(aux)
print(posi)
