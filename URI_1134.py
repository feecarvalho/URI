number = 0
alcool = 0
gas = 0
oil = 0

while number != 4:
    number = int(input())
    if number == 1:
        alcool += 1
    elif number == 2:
        gas += 1
    elif number == 3:
        oil += 1
    elif number > 4 or number < 0:
        number = 0

print('MUITO OBRIGADO')
print('Alcool: %d' % alcool)
print('Gasolina: %d' % gas)
print('Diesel: %d' % oil)
