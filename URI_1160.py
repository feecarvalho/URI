t = int(input())
anos = 0

while t > 0:
    values = input().split(' ')
    pa, pb, g1, g2 = values
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    while pa <= pb:
        pa = pa + int((pa * (g1 / 100)))
        pb = pb + int((pb * (g2 / 100)))
        anos += 1
        if anos > 100:
            break
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print('%d anos.' % anos)
    anos = 0
    t -= 1
