val = input().split(' ')
P, N = val
P = int(P)
N = int(N)
alt = [int(x) for x in input().split()]
r = ''
while len(alt) == N:
    for i in range(N - 1):
        if alt[i] <= alt[i + 1]:
            if alt[i] + P >= alt[i + 1]:
                r = 'YOU WIN'
            else:
                r = 'GAME OVER'
                break
        elif alt[i] >= alt[i + 1]:
            if alt[i] - alt[i + 1] <= P:
                r = 'YOU WIN'
            else:
                r = 'GAME OVER'
                break
    print(r)
    break
