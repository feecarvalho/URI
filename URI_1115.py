values = input().split(' ')
x, y = values
x = int(x)
y = int(y)

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print('primeiro')
    elif x > 0 and y < 0:
        print('quarto')
    elif x < 0 and y < 0:
        print('terceiro')
    else:
        print('segundo')

    values = input().split(' ')
    x, y = values
    x = int(x)
    y = int(y)
