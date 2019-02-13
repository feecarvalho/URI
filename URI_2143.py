while True:
    t = int(input())
    if t == 0:
        break
    for i in range(0, t):
        n = int(input())
        if n % 2 != 0:
            print(n * 2 - 1)
        else:
            print(n * 2 - 2)
