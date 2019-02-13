x = int(input())
y = int(input())

aux = 0

for num in range((y + 1), x):
    if (num % 2 != 0):
        aux += num
print(aux)
