n = int(input())
result = 0
x = n - 4
while x > 0:
    result += x
    x -= 1
print((n - 3) * 2 + result)
