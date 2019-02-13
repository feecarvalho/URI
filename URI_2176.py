bit = input()
cont = bit.count('1')
if cont % 2 == 0:
    print('{}{}'.format(bit, 0))
else:
    print('{}{}'.format(bit, 1))
