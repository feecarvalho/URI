x = int(input())
z = int(input())
valores = 0
total = 0
while z <= x:
    z = int(input())

while total < z:
    total += x
    x += 1
    valores += 1

print(valores)
