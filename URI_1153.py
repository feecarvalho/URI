n = int(input())
fat = n
total = 0
for num in range(1, n):
    fat *= (n - num)
    total += fat
print(fat)
