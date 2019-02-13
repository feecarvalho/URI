while True:
    try:
        L = int(input())
        V = input().split(' ')
        V = list(map(int, V))
        if max(V) < 10:
            print('1')
        elif max(V) >= 10 and max(V) < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break
