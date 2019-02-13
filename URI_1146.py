n = int(input())
value = []
while n != 0:
    for num in range(1, n + 1):
        value.append(num)
    print(*value, sep=' ')
    value = []
    n = int(input())
