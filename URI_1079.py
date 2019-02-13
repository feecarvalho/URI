N = int(input())

for num in range(0, N):
    ent = input().split(' ')
    a, b, c = ent
    media = ((float(a) * 2) + (float(b) * 3) + (float(c) * 5)) / 10
    print("%0.1f" % (media))
