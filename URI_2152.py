c = int(input())

while c > 0:
    entrada = [int(x) for x in input().split(' ')]
    h, m, o = entrada
    if o == 1:
        print('{:02}:{:02} - A porta abriu!'.format(h, m))
    else:
        print('{:02}:{:02} - A porta fechou!'.format(h, m))
    c -= 1
