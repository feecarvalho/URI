values = list(map(int, input().split()))
a = values[0]
n = values[1]
aux = 2
total = 0
while n <= 0:
    n = values[aux]
    aux += 1

for num in range(0, n):
    total += a + num
print(total)
