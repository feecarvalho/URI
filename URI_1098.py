J = 1
I = 0
for i in range(0, 3):
    print('I=%d J=%d' % (I, J))
    J += 1
J = 1
while True:
    I += 0.2
    J += 0.2
    if (I > 1.8 or I == 1.0):
        print('I=%0.0f J=%0.0f' % (I, J))
        print('I=%0.0f J=%0.0f' % (I, J + 1))
        print('I=%0.0f J=%0.0f' % (I, J + 2))
    else:
        print('I=%0.1f J=%0.1f' % (I, J))
        print('I=%0.1f J=%0.1f' % (I, J + 1))
        print('I=%0.1f J=%0.1f' % (I, J + 2))

    if I > 1.8:
        break
