ent = [int(x) for x in input().split(' ')]
for i in range(ent[1]):
    teste = input()
    if teste == 'fechou':
        ent[0] += 1
    else:
        ent[0] -= 1
print(ent[0])
