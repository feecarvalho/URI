d = int(input())

anos = d / 365
ra = d % 365
meses = ra / 30
dias = ra % 30

print('%d ano(s)\n%d mes(es)\n%0.0f dia(s)' % (int(anos), int(meses), float(dias)))
