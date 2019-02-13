ini_dia = input().split(' ')
ini_hora = input().split(' : ')

fim_dia = input().split(' ')
fim_hora = input().split(' : ')

duracao = ((int(fim_dia[1]) * 86400) + (int(fim_hora[0]) * 3600) + (int(fim_hora[1]) * 60) + (int(fim_hora[2]))) - (
        (int(ini_dia[1]) * 86400) + (int(ini_hora[0]) * 3600) + (int(ini_hora[1]) * 60) + (int(ini_hora[2])))
duracao_dias = float(duracao / 86400)
duracao_horas = float(duracao % 86400) / 3600
duracao_minutos = float(duracao % 3600) / 60
duracao_segundos = float(duracao % 60)

print('%0d dia(s)' % duracao_dias)

print('%d hora(s)' % duracao_horas)

print('%d minuto(s)' % duracao_minutos)

print('%d segundo(s)' % duracao_segundos)
