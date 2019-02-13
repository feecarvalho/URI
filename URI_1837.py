val = input().split(' ')

a, b = val
a = int(a)
b = int(b)

if b > 0:
    print(a // b, a % b)
else:
    print((a // (b * -1)) * -1, a % (b * -1))
