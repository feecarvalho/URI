S = 0
x = 1
y = 1

while x < 39:
    S += x / y
    x += 2
    y *= 2

print('%0.2f' % S)
