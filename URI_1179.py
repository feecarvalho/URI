par = []
impar = []
cont = 15

while cont > 0:
    x = int(input())
    if (x % 2) == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) == 5:
        for num in range(0, 5):
            print('par[%d] = %d' % (num, par[num]))
        par = []
    elif len(impar) == 5:
        for num in range(0, 5):
            print('impar[%d] = %d' % (num, impar[num]))
        impar = []
    cont -= 1

for num in range(0, len(impar)):
    print('impar[%d] = %d' % (num, impar[num]))
for num in range(0, len(par)):
    print('par[%d] = %d' % (num, par[num]))
