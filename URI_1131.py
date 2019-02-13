def get_inputs():
    inp = input().split(' ')
    gols_inter, gols_gremio = inp
    return gols_inter, gols_gremio


def redo():
    print('Novo grenal (1-sim 2-nao)')
    X = int(input())
    if X == 1:
        return True
    elif X == 2:
        return False


total = 0
sum_inter = 0
sum_gremio = 0
draw = 0

while True:
    x, y = get_inputs()
    total += 1
    if x > y:
        sum_inter += 1
    elif y > x:
        sum_gremio += 1
    else:
        draw += 1
    x = redo()
    if x == False:
        break

print('%d grenais' % total)
print('Inter:%d' % sum_inter)
print('Gremio:%d' % sum_gremio)
print('Empates:%d' % draw)

if sum_inter > sum_gremio:
    print('Inter venceu mais')
elif sum_gremio > sum_inter:
    print('Gremio venceu mais')
elif sum_inter == sum_gremio:
    print('Nao houve vencedor')
