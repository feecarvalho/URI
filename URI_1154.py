idade = int(input())
idade_list = []
idade_list.append(idade)
calc = 0

while idade > 0:
    idade = int(input())
    if idade > 0:
        idade_list.append(idade)

for num in idade_list:
    calc += num

calc = calc / len(idade_list)
print('%0.2f' % calc)
