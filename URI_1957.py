num = int(input())
num = hex(num).upper().split('X')
print(*num[1:], sep='')
