N = int(input())
total = 0
for num in range(N):
    ped = [float(x) for x in input().split(' ')]
    if ped[0] == 1001:
        total += ped[1] * 1.50
    elif ped[0] == 1002:
        total += ped[1] * 2.50
    elif ped[0] == 1003:
        total += ped[1] * 3.50
    elif ped[0] == 1004:
        total += ped[1] * 4.50
    elif ped[0] == 1005:
        total += ped[1] * 5.50
print('{:.2f}'.format(total))
total = 0
