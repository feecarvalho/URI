QT = int(input())
for i in range(QT):
    esc = input().split(' ')
    val = input().split(' ')
    x, y = val
    x = int(x)
    y = int(y)
    n1, e1, n2, e2 = esc

    if e1 != e2:
        if e1 == 'PAR':
            if (x + y) % 2 == 0:
                print(n1)
            else:
                print(n2)
        if e1 == 'IMPAR':
            if (x + y) % 2 != 0:
                print(n1)
            else:
                print(n2)
    else:
        break
