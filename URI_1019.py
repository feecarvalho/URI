N = int(input())
horas = N / 3600
minutos, segundos = 0

if horas < 0:
    horas = 0
else:
    minutos = N % 3600

minutos = minutos / 60
if minutos < 0:
    minutos = 0
else:
    segundos = N % 60

print("%d:%d:%d" % (int(horas), int(minutos), segundos))
