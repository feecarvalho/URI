nome = str(input())
salario_fixo = float(input())
total_vendas = float(input())

salario_total = (total_vendas * 0.15) + salario_fixo

print('TOTAL = R$ %0.2f' % salario_total)
